def selection_sort(arr1):
    for i in range(len(arr1)):
        minidexofval=i
        print("index of 1st element",minidexofval)
        for j in range(i+1,len(arr1)):
            print("loop of j starts")
            print("if second element is less than current loop starts" \
                "position",arr1[j],"less than",arr1[minidexofval])
            if arr1[j]<arr1[minidexofval]:
                minidexofval=j
                print("position of 1st elemnt should be second",minidexofval)
        arr1[i], arr1[minidexofval] = arr1[minidexofval], arr1[i]
        print("interchange the actual with where it belongs",arr1)
    return arr1

print(selection_sort([8,2,4,3,7,5,6,9,1]))
print("pick and drop at the right position" \
"logic - pick the position compare to right" \
"if small pick the position of that element and move forward" \
"if any small comes again, then pick its position" \
"replace it at the position where the smallest is," \
"actually we are looking for smallest")