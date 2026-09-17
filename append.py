def add_item(inventory, item):
    inventory.append(item)   # modifies the actual list object

items = ["sword"]
add_item(items, "shield")
print(items)   # ['sword', 'shield'] — changed! No return/reassignment needed