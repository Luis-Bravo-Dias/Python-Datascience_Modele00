ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

list_tuple = list(ft_tuple)
list_tuple[1] = "Portugal!"
ft_tuple = tuple(list_tuple)

ft_set.clear()
ft_set.add("Lisbon!")
ft_set.add("Hello")

ft_dict["Hello"] = "42Lisboa!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)