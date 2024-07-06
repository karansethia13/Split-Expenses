from itertools import combinations

def find_zero_sum_subsets_dict(dictionary):
    def backtrack(start, current_subset_keys, current_subset_values, remaining_sum, used):
        if remaining_sum == 0 and current_subset_values:
            result.append(list(current_subset_keys))
            return
        if start == len(keys) or remaining_sum > 0:
            return

        for i in range(start, len(keys)):
            if not used[i]:
                used[i] = True
                current_subset_keys.append(keys[i])
                current_subset_values.append(dictionary[keys[i]])
                backtrack(i + 1, current_subset_keys, current_subset_values, remaining_sum + dictionary[keys[i]], used)
                current_subset_keys.pop()
                current_subset_values.pop()
                used[i] = False
    
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    result = []
    used = [False] * len(keys)
    backtrack(0, [], [], 0, used)

    # Helper function to check if the subsets cover all elements exactly once
    def covers_all_elements(subsets, original_dict):
        element_count = {}
        for subset in subsets:
            for key in subset:
                value = original_dict[key]
                if key in element_count:
                    element_count[key] += 1
                else:
                    element_count[key] = 1
        for key in original_dict:
            if key not in element_count or element_count[key] != 1:
                return False
        return True

    # Finding the maximum number of non-overlapping zero-sum subsets
    max_subsets = []
    for i in range(1, len(result) + 1):
        for subset_combination in combinations(result, i):
            combined_keys = sum(subset_combination, [])
            combined_values = [dictionary[key] for key in combined_keys]
            if sorted(combined_values) == sorted(values):
                if covers_all_elements(subset_combination, dictionary):
                    if len(subset_combination) > len(max_subsets):
                        max_subsets = subset_combination

    # Convert the result to an array of dictionaries
    array_of_dicts = [{key: dictionary[key] for key in subset} for subset in max_subsets]
                        
    return array_of_dicts

def transact(payment_dict, transactions):
    while(payment_dict):
        first_key = next(iter(payment_dict))  
        first_value = payment_dict[first_key]  
        last_key = list(payment_dict.keys())[-1] 
        last_value = payment_dict[last_key]  
        
        if(first_value * -1 == last_value):
            transactions.append((first_key, last_key, last_value))
            payment_dict.pop(first_key)
            payment_dict.pop(last_key)
        elif(first_value * -1 > last_value):
            transactions.append((first_key, last_key, last_value))
            payment_dict[first_key] += last_value
            payment_dict.pop(last_key)  
            payment_dict = dict(sorted(payment_dict.items(), key=lambda item: item[1]))
        else:
            transactions.append((first_key, last_key, -1*first_value))
            payment_dict[last_key] += first_value
            payment_dict.pop(first_key)
            payment_dict = dict(sorted(payment_dict.items(), key=lambda item: item[1]))
        


payments = {}
while True:
    try:
        num_friends = int(input("Enter the number of friends: "))
    except:
        print("Enter an integer!")
        continue
    else:
        break
for i in range(num_friends):
    friend = input("Enter the name of friend {}: ".format(i+1))
    payments[friend] = 0

i = 1 
while(True):
    print("Transaction {}".format(i))
    try:
        friend = input("Who did the payment: ")
        payment=int(input(f"Enter {friend}'s payment: "))
        payments[friend] += payment
    except:
        print("Enter a valid person!")
        continue
    i += 1
    fwd = input("Do you want to add another transaction? (y/n) ")
    if fwd == 'n':
        break
    
print(payments)

total_sum = sum(payments.values())
average = total_sum / num_friends
payments = {key: value - average for key, value in payments.items()}
keys_to_remove = [key for key, value in payments.items() if value == 0]

# Remove keys from the dictionary
for key in keys_to_remove:
    del payments[key]

payments = dict(sorted(payments.items(), key=lambda item: item[1]))
print(payments)

# Example usage
payments_divided = find_zero_sum_subsets_dict(payments)
for subset_dict in payments_divided:
    print(subset_dict)
    
transactions =[]
for subset_dict in payments_divided:
    transact(subset_dict, transactions)

for transaction in transactions:
    print(f"{transaction[0]} gives {transaction[2]} to {transaction[1]}")