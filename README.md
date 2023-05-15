# Low-Level-Design

## Design Patterns

### Creational Patterns:

Singleton: Ensures that only one instance of a class is created and provides a global point of access to it.

Factory Method: Defines an interface for creating objects, but allows subclasses to decide which class to instantiate.

Abstract Factory: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

### Structural Patterns:

Adapter: Allows objects with incompatible interfaces to work together by providing a common interface.

Decorator: Dynamically adds new behavior to an object by wrapping it in an additional object.

Facade: Provides a simplified interface to a complex system, acting as a high-level interface to a subsystem of classes.

### Behavioral Patterns:

Observer: Defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

Strategy: Encapsulates interchangeable behaviors and allows selecting one at runtime.

Command: Encapsulates a request as an object, thereby allowing parameterizing clients with different requests, queueing or logging requests, and supporting undoable operations.

### Architectural Patterns:

MVC (Model-View-Controller): Separates the presentation layer (view) from the business logic (model) and user input handling (controller).

MVVM (Model-View-ViewModel): Similar to MVC, but introduces a separate model representation (view model) for the view, enabling better separation of concerns.

Repository: Provides an abstraction layer between the data access layer and the business logic layer, managing data retrieval and persistence.

### Concurrency Patterns:

Mutex: Provides mutually exclusive access to a shared resource, allowing only one thread to access it at a time.

Semaphore: Limits the number of threads that can access a resource concurrently.

Producer-Consumer: Coordinates the interaction between producer and consumer threads, ensuring data exchange without conflicts.





