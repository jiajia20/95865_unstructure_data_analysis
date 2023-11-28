################ DO NOT CHANGE ######################
import re

def is_contained_in_order(A, B):
    A = re.sub(r'\W+', '', A).lower()
    B = re.sub(r'\W+', '', B).lower()
    i = 0  # Index for string A
    for j in range(len(B)):  # Index for string B
        if A[i] == B[j]:  # If characters match
            i += 1  # Move to next character in A
            if i == len(A):  # If all characters in A found in B in order
                return True
    return False  # If not found

def approximate_match(A, B):
    return is_contained_in_order(A, B) or is_contained_in_order(B, A)

def approximate_unique_entity_label_pairs(entities_of_specific_question):
    unique_entities_in_question_without_approx_match = sorted(list(set(entities_of_specific_question)))
    indices_to_delete = set()
    n = len(unique_entities_in_question_without_approx_match)
    for idx1 in range(n):
        for idx2 in range(idx1 + 1, n):
            entity1, label1 = unique_entities_in_question_without_approx_match[idx1]
            entity2, label2 = unique_entities_in_question_without_approx_match[idx2]
            if label1 == label2 and approximate_match(entity1, entity2):
                indices_to_delete.add(idx2)
    for idx in sorted(indices_to_delete, reverse=True):
        del unique_entities_in_question_without_approx_match[idx]
    return unique_entities_in_question_without_approx_match
################ DO NOT CHANGE ######################