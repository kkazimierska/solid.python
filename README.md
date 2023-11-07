
## [SOLID Principles](https://en.wikipedia.org/wiki/SOLID) explained in Python with examples.

* [Single Responsibility Principle](https://github.com/heykarimoff/solid.python/blob/master/1.srp.py)
[Facade Pattern](https://refactoring.guru/design-patterns/facade)

## Task 1. Refactor class to comply with S(OLID) principle.
Go to `task_refactor.py`.
**Hint**: Remove pay method to the class responsible for processing the payment.
Separate the pay methods in different functions. Evaluate the `pay_debit`.

* [Open/Closed Principle](https://github.com/heykarimoff/solid.python/blob/master/2.ocp.py)

## Task 2. Refactor class to comply with (S)O(LID) principle.


**Hint**:
If we want to add extra payment method we need to modify the payment processor class by adding functions.
Define subclass of `PaymentProcessor` for each payment type.
Add **PayPal** payment type.

* [Liskov Substitution Principle](https://github.com/heykarimoff/solid.python/blob/master/3.lsp.py)

## Task 3. Refactor class to comply with SO(L)ID principle.
**PayPal** doesnot work with security but with e-mail address.

We are abusing **pay** type PaymentProcessor method - to do something different than **suppose to**.
Here the **argument** responsibility.
This is violating **LS** priniciple.

**Hint**: Add initializer to it to depend on email or security code.
Later, different payment processor sub-class will have extensibility to depend on different attributes via sub-class init. (Pay does not depend on `security_code`, but on `attribute` initizalized in `init`.)

* [Interface Segregation Principle](https://github.com/heykarimoff/solid.python/blob/master/4.isp.py)

Interfaces Segragation means it is better to have several specific interfaces than one general one purpose interface.

## Task 4. Refactor class to comply with SOL(I)D principle.

Extend `PaymentProcessor` class by sms auth method.
The problem is that the `Credit Card` payment method does not include sms auth.

Issue with generic like `PaymentProcessor` interfaces is that
they are not always applicable to subclasses.
In this case not all subclasses support 2-FA
It is better to add subclass of `PaymentProcessor` that enables 2-FA ( that have more meaningful behaviour).
This is **interface segregation**.


* [Dependency Inversion Principle](https://github.com/heykarimoff/solid.python/blob/master/5.dip.py)



