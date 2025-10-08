import marimo

__generated_with = "0.16.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import itertools as itertools
    import pandas as pd
    return itertools, mo, np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Iterables, iterators, and basic functional programming

    ## Goals

    - Understand, create and manipulate iterable objects in Python
    - Understand the conceptual division of iterables into ordered and unordered collections
    - Express (un/)ordered collections, and operations on them, both mathematically and in Python
    - Have a basic idea of functional programming styles and their advantages
    - *(only in Julia option, Pluto notebooks)* Understand and use the concepts of induction and recursion, both in programming and in proving/expressing mathematical concepts.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Iteration
    ### Iterator objects
    - We previously encountered sets: unordered collections of *things* (e.g. numbers, strings). Imagine sets as a bag.
    - We can take individual set elements out of the bag, perhaps to do some operation on them. We can **iteratively** take out elements of the set. So a set is an example of an **iterable**. 
    - An **iterator** is an object that does *something* to an iterable. See example below:
    """
    )
    return


@app.cell
def _():
    S = set((1,2, 5)) #iterable
    return (S,)


@app.cell
def _(S):
    iter = (x*x for x in S) #iterator. It hasn't been used yet: it's just an expression (a 'generator' expression.). Think of it as a 'promise'. Even if S were massive, it wouldn't takeany memory.
    sum(iter)  #the iterator is used. this method of coding never explicitly allocates memory to hold a new set with x*x instead of x. so it's efficient.
    return


@app.cell
def _(S):
    sc = {x*x for x in S} # curly brackets are a 'set comprehension': they make a new set by applying the transformation to each element of the set
    sc # running sum(sc) would be the same as running sum(iter). But it's less efficient: you allocated an unnecessary set.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""### Notation for iteration in mathematics
                     In mathematics, we also have to formulate operations on collections of things. For instance:
    	$$\sum_{x \in S} x^2$$
    	is the mathematical expression equivalent to `sum(iter)`:

    	- The $\sum$ symbol means `sum over`.

    	- The subscript $x \in S$ denotes the elements to sum over. In this case, we iteratively take each element in $S$, call it $x$, and add $x^2$ to our running total. """),kind="info" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""    ### Product

    	- Similarly 
    	$$\prod_{x \in S} x^2$$
    	is the product of the elements in $S$, equivalent to `prod(iter)`.

    	- Similarly, $$\{x^2: x \in S \}$$ or 

    	$$\{x^2\}_{x \in S}$$ 
    	is equivalent to `Set(iter)`. Remember that curly braces denote sets. 
    """),kind="info" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""### Notation for cardinality
    	The **cardinality** of a set is the number of elements in the set. The notation for the cardinality of a set $S$ is  	$$|S|$$
                      """),kind="info" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Questions" : r"""
    	- Fill in the `cardinality`  function below. It should return the number of elements in any set given as input.
        - Ideally, make it one line of code that uses the `sum` function!
        """})
    return


@app.cell(hide_code=True)
def _(missing):
    def cardinality():
        return missing
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Answer" : mo.ui.code_editor("""
    def cardinality(some_set): 
        return sum(1 for el in some_set)""")})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Conditional iterators
    We can also add **conditions** to iterators. We only take the element from the set if the expression after `if` evaluates to true. 
    - See the self-explanatory code below. 
    - Note that by using `and` statements  we can add any number of conditions. 'or' statements also useful!
    """
    )
    return


@app.cell
def _(S):
    conditional_iter = {x*x for x in S if x%2==1 and x>3} #x%2 means x mod 2
    conditional_iter
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ### Mathematical notation

    Here are some ways to write `conditional_iter` in maths. Notice that the semicolon acts as an `and`  (although you could also literally write the word and). 

    $$C = \{ x^2  : x \in S ; \quad x > 3; \quad x \mod 2 = 1 \}$$
    $$C = \{x^2 : x \in S \cap T \cap U\}$$
    where $T = \{x : x >3\}$ and $U = \{x: x \mod 2 = 1 \}$

    Notice that mathematical notation doesn't unfortunately distinguish between the two meanings of equals: assignment and conditional equality, unlike Python.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Question (optional)" : r"""
        Consider the infinite sequence of numbers: $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dots$. Consider a set that contains all of these numbers. Express their sum in mathematical notation.
        """})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Answer " : r"""so many ways!EG 
        $$\sum_{i=1}^{\infty} \frac{1}{i^2}$$ 
        $$\sum_{x \in S} \frac{1}{x^2}$$ 
        where $S = \{ x : \exists y \in \mathbb{N}: x = y^2 \}$ or $S = \{x^2 : x \in \mathbb{N}\}$ """})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Nesting Iterators and lambda functions
    - We can chain iterators together 
    - View the code below. You will need to look up anonymous (lambda) functions, to understand it.
    - predict what the value `max(transf)` will yield. You can uncomment it to see if you're correct
    - 
    *Note that if the set below were really large, this type of coding saves allocation of memory, as you never need to make any intermediate sets/collections (which cost memory) to do the computation*
    """
    )
    return


@app.cell
def _():
    def pow_iter(set):
        return (lambda x:x**n for n in set)

    transf = (el(2) for el in pow_iter({1,2,5}))
    # max(transf)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Questions" : r"""
        - Explain why/when a lambda function might be preferable to a standard (`def`) function 
    	- Write `pow_iter` out in mathematical notation
        """})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Answer 1" : r""" lambda functions are anonymous: they don't have a name. when building lots of functions iteratively, like in pow_iter, there is no need to provide a name. this makes the code more streamlined than is possible when using named functions""", "### Answer 2" : r"""$f(n,S) = \{x \to x^n \quad \forall n \in S\}$"""})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Map and filter

    #### Example
    I have a huge dataset. I want to return only the contents whose square root is greater than 10. Then I want to reverse their order. Then I want to multiply them by 2.

    **Bad way**: 

    1. Make a new dataset consisting of the square root of the old dataset (wastes memory and time ). EG `intermediate_dataset = [np.sqrt(el for el in dataset)]`
    2. Extract elements greater than 10. EG `intermediate2 = intermediate_dataset[intermediate_dataset > 10]`
    3. Reverse order: `intermediate3 = intermediate2[::-1]`
    4. Multiply: `final_dataset = 2*intermediate3`


    *Notice that each intermediate step above allocates a new intermediate dataset in memory, which is wasteful of memory and time. Huge issue if your dataset is gigabytes!*


    **Good way**

    1. Make a function that applies all of these steps in one go, avoiding the allocation of intermediate arrays.

    *But this sounds hard to read and write! (try if you like). `map` and `filter` come to the rescue to make it easy!*


    Let's think about `map` first. We call it like: `map(function, iterable)`. It applies the function to each element of the iterable. **Critically, it is lazy**. What does this mean? 

    - Look at the code below. Note that `xx` is just an expression holding the instructions for python on how to apply the map (a `map object`). Laziness means it hasn't actually done the mapping run the map, you can call `list(xx)`, which will run the mapping and allocate the contents into a list. 

    - Similarly, `yy` is a filter object. The first argument to filter is a function, whose output is a boolean (true or false). You apply each function to the iterable (a map object in this case). It filters out the objects that return false.

    In the code below, we ran a filter on a map object. Critically, at no point has the mapping or filtering actually been applied. `xx` and `yy` just hold instructions on how to do them. If you now run `list(yy)` in code, it will concretely allocate the output (i.e. do the mapping and filtering required).

    So for our example above, you could express each object as a map or a filter, and then chain them (as below). And then allocate only at the end! No intermediate datasets. Also readable and stylish.
    """
    )
    return


@app.cell(hide_code=True)
def _():
    _some_iterable = (1,2,3) #or a huge dataset
    xx= map(lambda el: el**2, _some_iterable)
    yy = filter(lambda el: el == 4, xx)
    (xx,yy)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Zipping iterators

    - Look up `zip` in the live docs. 
    - Zipping runs multiple iterators at the same time. 
    - Explain what the dictionary below (`alphabet_dict`) does.
    """
    )
    return


@app.cell
def _():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return (alphabet,)


@app.cell
def _(alphabet):
    alphabet_dict= dict(zip(alphabet, sorted(alphabet, reverse=True)))
    return (alphabet_dict,)


@app.cell
def _(alphabet_dict):
    alphabet_dict["b"]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    - There are extra modules with all sorts of [iteration utilities](https://pypi.org/project/iteration-utilities/). You can use them to do all sorts of iterator gymnastics. EG reversing iterators, cycling iterators indefinitely, etc. Mastering the elegant use of iterators is **very useful** when programming, and more importantly for this module helps with your 'maths mindset'. 

    - The nice thing about composing iterators and/or functions and applying them in one go, as we've been doing, is that you can build a complex pipeline that is **pure**. That is, it's behaviour depends only on the input data, and not other objects floating around in the code. This makes for fast, elegant, easily parallelisable code that is often easier to reason about and debug. We'll see examples later on.

    - It's an example of [**functional programming**](https://realpython.com/python-functional-programming/), which is a good programming style to have in your arsenal. Most Python code is instead written in an *object-oriented* style. 
    -   Of course, there is a lot more to functional programming, which you could go into if you like!

    -   I believe that the usefulness of functional programming is going to increase. Increasingly, programmers use frameworks like Jax, Cython, and Mojo, to turn (slow) interpreted Python code into (fast) just-in-time compiled code. This is easier if the compiler can understand and guarantee as much information on the code before compilation. Which is easier if most of your code is in functions and iterators that the compiler can reason about.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    ## Ordered Collections

    - Collections are sets of *things*. Ordered collections are sets of things which can be referred to by **indices** (singular is index). Each element of a collection has a position, the index (e.g. the first or fourth element), and can be referred to as such. **Unlike** sets, which are unordered.

    - For **any** ordered collection in Python, one accesses a numbered element through **square brackets**. EG `x[5]` will return the 5th element of the ordered collection `x`.

    - Python is a **zero-indexed** language: the first item of a collection `x` is `x[0]`, and the second is `x[1]`. In other words, you start counting from zero. I hate this! Mathematics (and e.g. Julia, Fortran, Matlab) are one-indexed, i.e. `x[1]` is the first element

    ### 1. Ranges
    - Look like this:`np.linspace(1,5,num=5)` or `range(1,5,1)`  (these two expressions define the same range!)
    - They correspond to evenly spaced numbers.  You should be using the live docs to look up how these functions work yourself at this point!
    - Ranges are **lazy** iterators. This means that defining a range doesn't allocate memory... if you write `range(1,100000,1)`, the computer doesn't actually store each of the intermediate numbers. Sometimes this is useful: `range(1,100000,1)` takes up the same memory as `range(1,10,1)`!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""### Tip
    Square brackets denote **indices of ordered collections**. Round brackets denote **inputs to functions**. Don't mix them up! See example below    	"""),kind="success" )
    return


@app.cell
def _():
    some_odd_numbers = range(1,39,2)
    return (some_odd_numbers,)


@app.function
def same_numbers_as_function(): #no inputs to this function
    return range(1,39,2)


@app.cell
def _(some_odd_numbers):
    some_odd_numbers[3] == same_numbers_as_function()[3]
    return


@app.cell
def _(some_odd_numbers):
    sum(some_odd_numbers) == sum(same_numbers_as_function()) #storing stuff in an inputless function is a good way of delaying execution of code if you ever need to!
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### 2. Arrays and tuples
    - Arrays are the **general purpose** tool for storing **mutable, ordered** collections of (any) objects (including arrays). You encapsulate the objects in square brackets, and separate them by commas.
    - Tuples are like arrays, but **immutable**. That is, you can't modify or add/remove to their contents after you've built them. 
    - The built-in Python arrays are called **lists**. You build them with square brackets. See below and read [here](https://www.w3schools.com/python/python_lists.asp)
    - You build a tuple with round brackets. See [here](https://www.w3schools.com/Python/python_tuples.asp)
    """
    )
    return


@app.cell
def _(mo):
    simple_array = [1,5,6, "orange"] # in python this is called a list. You can change the list. It's mutable!
    simple_tuple = ("orange", 6,5,1) #tuples cannot be changed after construction
    array_slider = mo.ui.slider(0, len(simple_array)-1,show_value=True)
    array_slider # slide and see what happens
    return array_slider, simple_array, simple_tuple


@app.cell
def _(array_slider, simple_array):
    simple_array[array_slider.value]
    return


@app.cell
def _(array_slider, simple_tuple):
    simple_tuple[array_slider.value]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    - Arrays are mutable in that you can change their size (i.e. add elements to them) (see below). This is **very slow**. Furthermore, the nature of Python makes array operations (i.e. doing operations such as summation on arrays) **very slow**.
    - A hack is to use numpy arrays (see below). Numpy codes lots of mathematical operations on numpy arrays in a fast language, like C++, meaning you can get most of the speed benefits of this fast language when using numpy arrays instead of Python lists. You [lose some flexibility](https://www.geeksforgeeks.org/python-lists-vs-numpy-arrays/).
    """
    )
    return


@app.cell
def _(np, simple_array):
    better_array = np.array(simple_array)
    very_computationally_inefficient_in_any_language = np.append(better_array, 45)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r""" ### **Key Concept**: Pass by reference vs pass by value
                Many online resources, e.g. [this one](https://nedbatchelder.com/text/names.html), explain the concept better than I could. **It's really important to understand the difference**. I'm going to illustrate the practical difference by example (below) and talk a bit about it in lectures. """),kind="info" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Questions" : r"""
        1. Inspect the code blocks 1 and 2 below, which build and change arrays and strings, respectively. Write a paragraph explaining the difference in behaviour between `an_array` and `a_string` when they are changed in their respective functions. Use the keywords "pass-by-reference" and "pass-by-value". 
        2. Can you give an example of how the behaviour exhibited in code block 1 might result in bugs in the code?
        """})
    return


@app.cell
def _():
    #code block 1
    an_array = [1,3,4]
    def change_array(an_array):
        an_array.append(42)
        print("an_array is currently", an_array)
        pass
    return an_array, change_array


@app.cell
def _(an_array, change_array):
    change_array(an_array)
    print("and now an_array is", an_array)
    return


@app.cell
def _():
    #code block 2
    a_string = "hello"
    def change_string(a_string):
        a_string = a_string + "bye"
        print("a_string is currently", a_string)
        pass
    return a_string, change_string


@app.cell
def _(a_string, change_string):
    change_string(a_string)
    print("and now a_string is", a_string)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Question" : r"""
        Use a single `for` loop on an iterable that zips locations and temps  below. Use this `for` loop to print out "in <location>, the sea temperature is <temp>", for each of the location-temperature pairs below
        """})
    return


@app.cell
def _():
    places = ("Shoreham-by-sea", "Worthing", "Brighton", "Eastbourne")
    temps = (16.4, 17.2, 18.3, 17.9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Answer" : mo.ui.code_editor(
        """for (loc, temp) in zip(places, temps):
        print(loc, "has a temperature of", temp)"""
    )})
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Tensors and Cartesian Indices

    - So far, we have considered ordered collections with a **single** indexing variable. E.G. the indexing variable $i$ in the vector $[i]_{i=1}^{100}$

    - However, it's often convenient to use **multiple** indexing variables. How do we refer to an element in a table? By it's row **and** column. The row/column number are separate indexing variables.

    $$A =
    \begin{bmatrix}
    A_{11} & A_{12} \\
    A_{21} & A_{22}
    \end{bmatrix}$$

    Thus in code, the bottom left entry of $A$ would be `A[2,1]`. IE 2nd row, 1st column.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r""" ### Important
    	From now on, we will refer to an ordered collection with $n$ indexing variables as an $n$-tensor, or an $n$-dimensional tensor

    So the table above is a two-tensor: to reference its elements we need two indexing variables (row and column number). 

    We will sometimes have to deal with objects that have **more than two indexing variables!:**

    ![](https://codecraft.tv/courses/tensorflowjs/tensors/what-are-tensors/img/designed/3d-tensor.jpg)
    """),kind="danger" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""### Important
    	What about an element without indexing variables, like the number 5? This is a **zero-tensor**. We require $0$ indexing variables to access the element. 
    """),kind="danger" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""### Notation
    	    	Commonly used terms for different tensors:

    	**1-tensor** $\leftrightarrow$ **Vector**

    	**2-tensor** $\leftrightarrow$ **Matrix**


    	The 1st/2nd indices of a matrix are called its rows and columns. The 3rd index of a 3-tensor is often referred to as a **layer** (as you see in a neural network) 

    	Learn these!!!
    	"""),kind="info" )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### Example of 3d tensor in Numpy""")
    return


@app.cell
def _(np):
    shape = (3, 4, 5)
    # Create a 3D array of random numbers using list comprehension
    random_3d_array = np.array([[[np.random.random() for _ in range(shape[2])] 
                               for _ in range(shape[1])] 
                               for _ in range(shape[0])])
    return (random_3d_array,)


@app.cell
def _(mo, np, random_3d_array):
    mo.output.append(random_3d_array[2,1,1]) # access an individual element
    mo.output.append(np.mean(random_3d_array, axis = (0,1))) #mean of each layer (i.e. averaged across rows and columns)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Functional programming on collections

    What happens when we do data analysis? 

    - Data usually amounts to an ordered collection of **things**. For instance, an excel spreadsheet is a 2-tensor, ordered by rows and columns. So data is an iterable!
    - Data cleaning/processing/analysis usually amounts to a sequence of operations on the data. One could write a script that iteratively transforms the data by doing the desired operations. EG
          1. Clean the data by removing outliers and unnecessary datapoints
          2. Convert the data (e.g. from centimetres to metres)
          3. Analyse the data by finding its statistics (mean, variance, whatever)

    - The straightforward way to do this is to write a long block of code that does these operations in turn. But this has a few issues
        1. You're creating new intermediate collections (e.g. of the converted data), which is slow and wastes space. And what if you accidentally corrupt one of the intermediate collections? (e.g. with the pass by reference issues above)
        2. Debugging a long block of code is hard, and bugs **will** permeate all code you write.


    Instead let's play with a toy example using a functional programming paradigm. This makes use of `map`, `reduce`, and `filter`, which are **really good to know about and exploit in your programming**.
    [read this first](https://book.pythontips.com/en/latest/map_filter.html)

    - Inspect the code below, so you can understand what and why each line is doing. You'll have to do something similar yourself afterwards! Make liberal use of the live docs and google.
    """
    )
    return


@app.cell
def _(np):
    ## we want to convert this list of temperatures to celsius, and do some simple operations on it:

    temperatures_fahrenheit = np.array([32, 45, 60, 80, 90, 100, 105, 40, 35, 28, 50, 70, 72, 85, 100, 110, 95, 90, 88, 92, 76, 65, 58, 54, 48, 36, 30, 25, 20, 15])

    def celsius_converter(number):
        return (number-32)*(5/9)
    return celsius_converter, temperatures_fahrenheit


@app.cell
def _(celsius_converter, itertools, temperatures_fahrenheit):
    # a LAZY conversion to celsius. This returns an iterator, rather than allocating a concrete new dataset in celsius
    def celsius_iterator():
        return map(celsius_converter, temperatures_fahrenheit)

    ## filter out the hot (by british standards) days (again lazy)
    def hot_days():
        return filter(lambda x: x > 25, celsius_iterator())

    ## find temperature differences between days
    def temp_differences():
        lagged_iterator = itertools.islice(celsius_iterator(), 1,None) #another iterator starting from the second ([1]) element.
        diff = (tomorrow-today for (today, tomorrow) in zip(celsius_iterator(), lagged_iterator))
        return diff
    return hot_days, temp_differences


@app.cell
def _(hot_days, mo, np, temp_differences):
    #list hot days if needed, by collecting the iterator elements (but usually wouldn't want to do this)
    mo.output.append(np.fromiter(hot_days(), int))
    #count hot days
    mo.output.append(sum(1 for el in hot_days()))
    #list temperature differences between days
    mo.output.append(np.fromiter(temp_differences(), int))
    # some functions, like np.std, need a concrete array rather than an iterator. Ideally, the numpy creators would amend this!
    mo.output.append(np.std(np.fromiter(temp_differences(),int)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    #### Things to note

    Important points that pop up from the toy example above:

    - A functional programming paradigm is to express each data transformation as a lazy (unevaluated) function on the iterable data. So an iterator. And then you can nest transformations to get each output you want.
    - This will end up in code that consists of a lot of small functions, which can be easily and individually debugged. The immutable, original data isn't modified, minimising corruption. The final results are just compositions of these functions. Intermediate transformations of the data are never stored in memory, which is great for large datasets.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Questions" : r"""
        - Look at the dataframe below, for information on some cars.
        - Usually you would analyse this using the functionality of Pandas dataframes. (Polars is even better!) For practice, we won't.
        - I've just extracted numpy vectors for the Miles-per-gallon (mpg) and horsepower components (see below)
        - Build a function that operates on these vectors, and finds the max mpg of the cars whose horsepower satisfies $h^2 < 10300$. Critically, **it shouldn't allocate any intermediate arrays**. It should just be a nesting of iterators. 
        - Hint: one iterator is going to need to filter out NaN values
        """})
    return


@app.cell
def _(pd):
    cars = pd.read_json(
        "https://raw.githubusercontent.com/vega/vega-datasets/master/data/cars.json"
    )
    return (cars,)


@app.cell
def _(cars):
    cars
    return


@app.cell
def _(cars, np):
    mpg = np.array(cars["Miles_per_Gallon"]) 
    hp = np.array(cars["Horsepower"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion({"### Answer" : mo.ui.code_editor("""
    def get_high_horsepower_mpgs():
        iterboth = zip(mpg, hp)
        fil = filter(lambda x: x[1]**2 > 10300, iterboth)
        filmpg = (x[0] for x in fil)
        no_nan_filmpg = filter(lambda x: ~np.isnan(x), filmpg)
        return max(no_nan_filmpg)
    get_high_horsepower_mpgs()
        """)})
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
