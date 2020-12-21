from abc import ABC, abstractmethod

class Observable(ABC):
    '''
    Abstract interface class for the observable
    '''
    def __init__(self, topics: list):
        self.topics = {topic:set() for topic in topics}
    
    @abstractmethod
    def subscribe(self, topic: str, observer_entity: str):
        pass

    @abstractmethod
    def unsubscribe(self, topic: str, observer_entity: str):
        pass

    @abstractmethod
    def notify(self, topic: str, message: str): 
        pass

class Observer(ABC):
    '''
    Abstract interface class for the observers
    '''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def receive_alert(self, message: str):
        pass

class Bridge(Observable):
    '''
    Concrete implementation of Bridge at a location

    There can be a different implementation for another bridge 
    at a different location and buisness logic can be 
    completely different
    '''
    def __init__(self, topic_list: list):
        super().__init__(topic_list)

    def subscribe(self, topic: str, observer_entity: Observer):
        self.topics[topic].add(observer_entity)

    def unsubscribe(self, topic: str, observer_entity: str):
        self.topics[topic].remove(observer_entity)

    def notify(self, topic: str, message: str): 
        for subscriber in self.topics[topic]:
            subscriber.receive_alert('{}: {}'.format(topic, message))

class Owner(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("Owner acknowledges the message: {}".format(message))


class Owner(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("Owner: {} ack to received msg: {}".format(self.name, message))


class StrucEngg(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("StructEngg: {} evaluating damage reported in: {}".format(self.name, message))


class TrafficEngg(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("TrafficEngg: {} metering adjusted for: {}".format(self.name, message))

class Pavers(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("Pavers: {} crew displatched to repair: {}".format(self.name, message))

class Electical(Observer):
    '''
    Concrete implementation of Observer abstract interface
    '''
    def __init__(self, name):
        super().__init__(name)

    def receive_alert(self, message: str):
        print("Electical: {} parts ordered: {}".format(self.name, message))

# create the observable/publisher/subject
brA = Bridge(['pavement', 'structure', 'light'])

# create observers/subscribers
owner_brA = Owner('CA_DOT')
struct_contractor = StrucEngg('BridgeExpert_inc')
traffic_contractor = TrafficEngg('ControlFlow_inc')
pav_contractor = Pavers('Paving_inc')
elec_contractor = Electical('Power_inc')

# Attach subscriber to relevant topic
brA.subscribe('pavement', owner_brA)
brA.subscribe('pavement', traffic_contractor)
brA.subscribe('pavement', pav_contractor)

brA.subscribe('structure', owner_brA)
brA.subscribe('structure', struct_contractor)
brA.subscribe('structure', traffic_contractor)

brA.subscribe('light', owner_brA)
brA.subscribe('light', elec_contractor)

# Notify subscriber to corresponding topic
print("\n*** Issue with road surface quality ***")
brA.notify('pavement', 'Pothole at mid location of span 42')
print("\n*** Issue with structural element ***")
brA.notify('structure', 'Crack detected next to Pier 6')
print("\n*** Issue with lights ***")
brA.notify('light', 'Time to replace all lights')
print("")
