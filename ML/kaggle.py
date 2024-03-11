def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [el > thresh for el in L]

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(0, len(meals)-1):
        for j in range(i+1, len(meals)):
            if meals[i] == meals[j]:
                return True
    return False 

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    result = []
    for i in range(len(doc_list)):
        if keyword.lower() in doc_list[i].lower().replace(".", "").replace(",", "").split():
            result.append(i)    
    return result

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    result = { keyword:word_search(doc_list, keyword) for keyword in keywords }
    return result

def hand_total(hand):
    """
    Return the total of a hand in Blackjack

    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    """
    total = 0
    count_of_aces = 0
    
    for item in hand:
        if item in ('J', 'Q', 'K'):
            total += 10
        elif item == 'A':
            count_of_aces += 1
            total += 11
        else:
            total += int(item)
    
    if total > 21 and count_of_aces > 0:
        total = total - count_of_aces * 11 + count_of_aces * 1

    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
      
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_1_total = hand_total(hand_1)
    hand_2_total = hand_total(hand_2)
    return hand_1_total <= 21 and (hand_1_total > hand_2_total or hand_2_total > 21)
    pass

print(blackjack_hand_greater_than(['K'], ['3', '4']))
print(blackjack_hand_greater_than(['K'], ['10']))
print(blackjack_hand_greater_than(['K', 'K', '2'], ['3']))
#print(input, result)
