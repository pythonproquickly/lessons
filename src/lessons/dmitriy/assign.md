Motivation:  You have been hired to build a booking quote system for
transporting packages. You will write this system in Python, as a terminal
application. You will use simple terminal IO (input and print) as a user
interface for now. Another developer in the future will convert this to a
server application that is front-ended with a browser (you don’t need to worry
about how this happens as it's not part of your work, but it can and should
influence how you build your system). The application you are building will
capture the following information:  * Name of the customer. * Package
description. * Are the contents dangerous? [Y/N] * Weight (kgs). * Volume (
cubic meters). * Required delivery date (month/date/year). * International
destination? [Y/N]  The application will then attempt to find the best way to
route the package (air / ground / ocean). The rules it will use are as follows:
* Packages can only be shipped if they weigh less than 10Kg **or** are smaller
than 5x5x5 meters (125 cubic meters). * If the package contains dangerous goods
it cannot be routed via air. * 'Urgent' means a package has to be delivered in
less than 3 business days. * If the package is urgent it will be routed via
air, if possible. * If the package is heavy or (towards the maximum end of the
boundaries set in 1 above), and is not urgent, it can be routed via truck (or
even ocean if it is for an international destination). * Air shipments cost $10
per kilogram or $20 per cubic meter, whichever is the highest. * Truck
shipments cost a flat rate of $25, or $45 if urgent. * Ocean shipments costs a
flat rate of $30. Your system will apply these rules to the booking and will
calculate alternative shipping options (or one, or possibly none, depending on
how the above rules affect the booking). The shipping options must be printed
in a clearly understood format, and should be appended to a booking_quotes.csv
file. There will be one row in the file for each quote. This application is to
be developed using an object oriented approach. It will require extensive
automated tests to ensure the above rules are correctly applied by the system.
Here is what you need to do:  * Use automated testing to validate the system
behaves as intended. * Develop the data capture functionality, paying careful
attention to any implied data needs. * Make sure the data is validated, so data
entry errors can be prevented as much as possible. * Build a menu so the system
is easy to use. * Ensure each booking has a unique id. * Make use of formatting
techniques to ensure that information reported to the screen is well laid out
and easy to understand. * Be sure each booking quote is stored in the csv file.
* Be sure to commit to local git frequently and use a virtual environment. Tips
* Be creative! Use this as an oportunity to reflect on everything you have
learned so far and apply it to application development. * Consider making your
user interface fully separated from the rest of the project. This will make it
easier to implement a new web-based interface later on without having to modify
the underlying implementation.
