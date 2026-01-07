# Сheck Your Code Against the Following Points

## Don't Repeat Yourself

Make sure you don't have duplicated lines or whole blocks of code. Use your `format_linter_error` function to avoid this.

Also, use the `format_single_linter_file` function to format a single file.

## Code Style

Use descriptive and correct variable names.

Good example:

```python
my_dict = {"one": "a", "two": "b"}
[(number + " " + letter) for (number, letter) in my_dict.items()]
```

Bad example:

```python
my_dict = {"one": "a", "two": "b"}
[(k + "  " + v) for (k, v) in my_dict.items()]
```

While creating a dictionary — write key-value pairs in a single row. The curly braces must be located in one of two options: open and start with the text or have a line break between the text. 

Good example:

```python
my_dict = {
	"greeting": "Good morning, have a nice day!", 
	"answer": "Good morning, thanks!"
}

```

Also a good example:

```python
my_dict = {"greeting": "Good morning, have a nice day!", 
	   "answer": "Good morning, thanks!"}
```

Bad example:

```python
my_dict = {"greeting": "Good morning, have a nice day!", 
	   "answer": "Good morning, thanks!"
}
```

