# Observer Design Pattern

This design pattern is applicable if you have an object (Observable) which multiple other entities want to monitor. It makes one go away from 'Pull' architecture where the interested parties keep asking for updates to 'Push' strategy where the Observable can let the Observers know if there is an update.

Sometimes observer pattern is referred to as a publisher-subscriber model in sense of a message queue where publisher and subscriber are loosely coupled through a message queue in the middle.

To make the discussion more tangible lets us take an example of a physical entity like a highway bridge. The bridge in our case is heavily instrumented with sensors and cameras and the owner of the bridge has hired multiple contractors to maintain the traffic flow, road surface, structural components, and electrical systems. The owner hires you as a programmer who applies state-of-art AI/ML and data interpretation techniques to come up with indicators that clearly tells what is happening with the bridge. To make this system responsive, your job is to let appropriate groups know that something related to them has gone wrong and they need to come and fix it.

To apply the observer pattern you will create a bridge object with few topics (the observable) and let different parties subscribe to these topics. For this example the topics can be:

| Topic         | Subscribers        |
|---------------|--------------------|
|road_surface   | owner, traffic_group, pavers|
|structural     | owner, structural_group, traffic_group|
|lights         | owner, electrical_group|

This way only parties with a direct interest in the issue get notified and they can take appropriate action without getting bombarded with issues that do not concern them.

As functions are 1st class citizens in Python we can do callbacks more easily as compared to other languages.
