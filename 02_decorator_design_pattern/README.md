## Decorator Design Pattern

This section's content and code are inspired by the Head First Design Pattern book.

The decorator design pattern is used to attach additional responsibilities to an object during runtime, as opposed to compile time. 

The pattern is intended to be used when there are few canonical objects and they can be combined/stacked in any number of ways to build a new object.For example, talking about the coffee shop example from the 'head first' book it is easy to visualize the benefits of this design pattern.

 Let's start with a small example where we have just one kind of coffee, say, "house blend - dark roast" and two add-ons, say, "Soy Milk" and "Whip Cream".

 To cover all variety of customer the code will have to have classes for:
- House Blend + Soy
- House Blend + Soy + Whip
- House Blend + Whip

but what if now there are customers who want 
- House Blend + 2*Soy 
- House Blend + 2*Soy + Whip
- can't even imagine the next order `...`

There can be an explosion of unique classes that need to be defined. This is where the Decorator pattern comes in handy.

For this particular example one can have "house blend - dark roast" as one of the canonical objects and "Soy Milk" and "Whip Cream" as decorator objects. This way we can have the innermost object of "house blend" decorated upon by any number of defined condiments in any order, any number of times.
