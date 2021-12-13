# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from korth_spirit.sdk import EventEnum

from .event import Event
from .translations import TRANSLATIONS


class EventBus:
    def _hook_aw_event(self, event: EventEnum) -> None:
        """
        Republish AW events to the bus.

        Args:
            event (Event): The event to publish and hook.
        """
        from aw.sdk import AW_CALLBACK, aw_event_set

        @AW_CALLBACK
        def mini_pub() -> None:
            self.publish(event)

        self._refs[event] = mini_pub
        aw_event_set(event, mini_pub)

    def __init__(self):
        self._refs = {}
        self._subscribers = {}

    def subscribe(self, event: EventEnum, subscriber: callable) -> "EventBus":
        """
        Subscribe to an event.

        Args:
            event (Event): The event to subscribe to.
            subscriber (callable): The subscriber to the event.

        Returns:
            EventBus: The event bus.
        """
        if event not in self._subscribers:
            self._subscribers[event] = []
            self._hook_aw_event(event)
        self._subscribers[event].append(subscriber)

    def unsubscribe(self, event: EventEnum, subscriber: callable) -> "EventBus":
        """
        Unsubscribe from an event.

        Args:
            event (Event): The event to unsubscribe from.
            subscriber (callable): The subscriber to the event.

        Returns:
            EventBus: The event bus.
        """
        if event in self._subscribers:
            self._subscribers[event].remove(subscriber)

        return self

    def publish(self, event: EventEnum, *args, **kwargs) -> "EventBus":
        """
        Publish an event.

        Args:
            event (Event): The event to publish.
            *args: The arguments to pass to the subscribers.
            **kwargs: The keyword arguments to pass to the subscribers.

        Returns:
            EventBus: The event bus.
        """
        translations = TRANSLATIONS.get(event, {})
        wrapped_event = Event(event, translations)
        if event in self._subscribers:
            for subscriber in self._subscribers[event]:
                subscriber(wrapped_event, *args, **kwargs)
        
        return self
