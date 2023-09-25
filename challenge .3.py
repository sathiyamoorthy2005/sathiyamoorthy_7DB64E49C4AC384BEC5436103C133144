def linearsearchproduct(productlist, targetproduct):
 indices = []
 
 for index, product in enumerate(productlist):
     if product == targetproduct:
       indices.append(index)
 
 return indices
 
#Example usage:
 
products =["shoes", "boot", "Loafer", "Shoes", "sandal", "shoes"]
 
target = "Shoes" 
 
target2='apple'
 
result= linearsearchproduct(products, target)
print(result)
 
