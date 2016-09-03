// When not in console, ; is needed at end of statement.
var foo = "bar"
foo.length			// -> 3
foo.charAt(1)			// -> "a"

// Print on console:
console.log("foo");

////////// Strings
var foo = "foo";
foo.toUpperCase();		// -> "FOO" (whole string)
foo.charAt(0).toUpperCase();	// -> "F"   (single char)

// For loop (like C):
for(var myVar = 1; myVar < 10; myVar++) {
    console.log("Well, whatever: " + myVar + "\n");
}

// While loop (like C):
while(myVar <= 10) {
    console.log(myVar + "\n");
    myVar++;
}

// If
if (condition) {
    // foo
} else {
    // otherwise
}

if (condition) {
    // foo
} else if (other_condition) {
    // bar
} else {
    // flappage
}

// Complex conditionals (AND / OR)
if (condition1 && condition2) { }
if (condition1 || condition2) { }

// Builtins
alert("Message");         // Pops up a window with message
confirm("Are you sure?"); // Pops up OK / Cancel window, returns true / false
var name = prompt("What's your name"); // Pops up input field window
typeof true;      // -> "boolean" (note - no parens on typeof)
typeof "fo";      // -> "string"
typeof 42;        // -> "number"
typeof undefined; // -> "undefined"
typeof null;      // -> "object"

// Functions
function sumOfCubes(a, b) {
    return a * a * a + b * b * b;
}

var fun = function foo(a, b) {	// Function pointer? Function builds only
    return a + b;		// when this line of code is reached.
};				// Note semicolon
fun(1, 2);			// Note: use name fun, not foo

// Anonymous functions
var fun = function (a, b) {	// Just skip function name
    return a - b;
};				// Note semicolon
alert(fun);			// Display function body

// map - looping over a list, generating a new list
var numbers = [1, 2, 3];
numbers.map(function (cellContents) { return cellContents * 2; });
// -> [2, 4, 6];

// Calling a returned function, the long way:
fun = buildFun();
fun();

// Calling a returned function, the short way:
buildFun()();

// Functions with an unknown / variable number of args:
function logThing() { // Notice, no args
    // 'arguments' is an array-like thing. Iteration is possible.
    for (var i = 0; i < arguments.length; i++) {
	console.log(arguments[i]);
    }
}

// Arrays
var myArray = [ "foo", "bar", "flap" ];
myArray[0];              // -> "foo"
myArray[0] = "Foo";
myArray.length;          // -> 3
myArray.pop();           // -> "flap" (deleting the last entry)
myArray.push("Flap");    // Appends "Flap" to the end of the array
myArray[1] = undefined;  // Make cell 1 empty - does not truncate array

myArray.shift();         // Remove and return first entry. Similar to
                         // pop(), except pop works with the last
                         // entry.

////////// Closures
//
// Closure variables are bound at the very last moment - meaning, they
// will retain the value they had just before return was called.

// Hoisting In JavaScript, you can call functions before they're
// defined (which in C is only possible if you have declared the
// function). However, when you use function *expressions* (read: var
// func = function() {...}), then you have to make sure you run the
// code that assigns the function to its variable ("func" in this
// case) *before* you call that function using the variable.

////////// Objects

// There are several ways to make objects.
// 
//// 1) "Object literal":
var myBox = { };
var myBox = { height: 8, width: 6, length: 10 };

//// 2) Using create:
//
// Using inheritance, you can create new objects using existing
// objects as prototypes:
var bag = { capacity: 10, weight: 10 };
var backpack = Object.create(bag); // bag == prototype ("parent")
bag.isPrototypeOf(backpack);	   // -> true
backpack.isPrototypeOf(bag);	   // -> false
Object.isPrototypeOf(backpack);	   // -> true (because it's not just
				   // -> parents, it's also
				   // -> grandparents etc)

//// Classes
//
// "A Class is a set of Objects that all share and inherit from the
// same basic prototype."
//
//  Constructors
//
// Functions starting with capital letter are class constructors.
function Bag(capacity, weight) {
    this.capacity = capacity;
    this.weight   = weight;
}

var myBag = new Bag(10, 5);
myBag				// -> Bag {capacity: 10, weight: 5 }

//// Properties
//
// To access one of the properties:
myBox.height;			// -> 8
myBox.height = 12;
myBox.weight = 24;		// Works on previously non-existing
				// properties too.
// You can also use brackets[] to access properties.
myBox["height"];		// -> 8
// With brackets, you can even use spaces in property names.
myBox["prop with space"] = 42;
// To delete / remove a property from an object. This completely
// removes the property, it doesn't just set it to undefined or
// somesuch.
delete myBox.heights;
// "delete" always returns true, whether the property existed or not.

// You can access properties of objects nested inside other objects:
myBox.book.title;
myBox["book"]["title"];

// Object methods
// First way to add a method:
var bag = {
    name: "Bag of Carrying",
    capacity: 30,
    contents: [ ],
  
    addContent: function (content) { // Methods are anon functions
	this.contents.push(content);
    }
};

// Second way to add a method:
bag.removeContent = function (content) {
    // foo
};

bag.addContents("shortsword of quickness");

// Enumeration - finding all properties in an object
var myObj = {
    size: 10,
    bulk: 20
};

for (myKey in myObj) {
    console.log(myKey + ": " + myObj[myKey]);
}

// If you refer to an undefined key in an object, you get "undefined",
// not an error.

////////// Inheritance
// In JavaScript, inheritance parents are called "prototypes", for some
// reason.  

// It is possible to add properties (methods or otherwise) to
// prototypes (parents), even if they're the "standard" prototypes
// like String, Array, etc:
String.proptotype.myNewFunc = function () { };
