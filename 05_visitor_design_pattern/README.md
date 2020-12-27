# Visitor Design Pattern

This pattern supports the open/close principle of SOLID principles. The pattern allows adding new functionality (methods) to classes of a collection of objects without altering those classes.


A very relatable application of this pattern is the `Save As` functionality in almost all software. For this example, let's take the example of Microsoft Excel. The main application can be reading in data from multiple formats, for this discussion we will take only two: csv, xlsx. The application allows the user to save the file into many different formats, for this example, we will only allow saving as xlsx, pdf. In this case, the csv and xlsx file objects are present as concrete implementations of the class hierarchy, and saving as xlsx and pdf are implemented as visitors to the class. Now if a new format (let say prn) for the `Save As` feature is introduced it is much easier to extend the functionality by adding another concrete implementation of the visitor abstract class.

