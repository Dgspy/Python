def reverse(seq):
	seq_type = type(seq)
	empty_seq = seq_type()
	if seq == empty_seq:
		return empty_seq
	rest = reverse(seq[1:])
	first_seq = seq[0:1]
	final_result = rest +first_seq
	return final_result
print(reverse([10,20,30,40]))
print(reverse("darkdevil of internet"))