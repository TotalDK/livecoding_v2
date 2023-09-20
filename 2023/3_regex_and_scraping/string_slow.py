s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque venenatis urna nibh, eget euismod quam pretium non. Proin lorem lectus, pellentesque ut elementum eu, sodales et velit. In in odio sed massa pharetra imperdiet ac vitae lectus. Phasellus consequat eu orci in elementum. Nunc mattis lorem lacus, nec interdum felis tincidunt ut. Morbi condimentum cursus mauris. Aliquam erat volutpat. Maecenas commodo maximus feugiat. Sed vel odio vitae metus feugiat molestie sed sit amet nisi. Sed in arcu ut felis ullamcorper aliquam. Proin eu lobortis arcu. Maecenas ultrices viverra nulla, ultricies imperdiet diam gravida nec. Curabitur mattis ultrices nunc non feugiat."

for iteration in range(100):
	print(iteration, f"(length {len(s)}; {2**iteration} Lorem Ipsums)")
	s *= 2

print(s)