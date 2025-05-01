class EventDispatcher:
    __listeners = {}

    @staticmethod
    def subscribe(event_name: str, listener):
        if event_name not in EventDispatcher.__listeners:
            EventDispatcher.__listeners[event_name] = []
        EventDispatcher.__listeners[event_name].append(listener)

    @staticmethod
    def unsubscribe(event_name: str, listener):
        if event_name in EventDispatcher.__listeners:
            EventDispatcher.__listeners[event_name].remove(listener)

    @staticmethod
    def notify(event_name: str, data: dict):
        if event_name in EventDispatcher.__listeners:
            for listener in EventDispatcher.__listeners[event_name]:
                listener.update(data)
