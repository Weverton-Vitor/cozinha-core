class EventDispatcher:
    __subscribers = {}

    @staticmethod
    def subscribe(event_name: str, listener):
        if event_name not in EventDispatcher.__subscribers:
            EventDispatcher.__subscribers[event_name] = []
        EventDispatcher.__subscribers[event_name].append(listener)

    @staticmethod
    def dispatch(event):
        listeners = EventDispatcher.__subscribers.get(event.name, [])
        for listener in listeners:
            listener(event)