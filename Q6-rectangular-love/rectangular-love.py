def intersection(rectA, rectB):

	a_lower_left = (rectA['left_x'], rectA['bottom_y'])
	a_upper_left = (rectA['left_x'], rectA['bottom_y'] + rectA['height'])
	a_upper_right = (rectA['left_x'] + rectA['width'], rectA['bottom_y'] + rectA['height'])
	a_lower_right = (rectA['left_x'] + rectA['width'], rectA['bottom_y'])
	
	b_lower_left = (rectB['left_x'], rectB['bottom_y'])
	b_upper_left = (rectB['left_x'], rectB['bottom_y'] + rectB['height'])
	b_upper_right = (rectB['left_x'] + rectB['width'], rectB['bottom_y'] + rectB['height'])
	b_lower_right = (rectB['left_x'] + rectB['width'], rectB['bottom_y'])

	horizontal_intersection_point_one = -1
	horizontal_intersection_point_two = -1

	# if b left intersects horizontally
	if b_upper_left[0] >= a_upper_left[0] and b_upper_left[0] <= a_upper_right[0]:
		horizontal_intersection_point_one = b_upper_left[0]
		horizontal_intersection_point_two = min(b_upper_right[0], a_upper_right[0])

	# if b right intersects horizontally
	if b_upper_right[0] >= a_upper_left[0] and b_upper_right[0] <= a_upper_right[0]:
		horizontal_intersection_point_one = max(b_upper_left[0], a_upper_left[0])
		horizontal_intersection_point_two = b_upper_right[0]

	vertical_intersection_point_one = -1
	vertical_intersection_point_two = -1

	# if b lower intersects vertically
	if b_lower_left[1] >= a_lower_left[1] and b_lower_left[1] <= a_upper_left[1]:
		vertical_intersection_point_one = b_lower_left[1]
		vertical_intersection_point_two = min(b_upper_left[1], a_upper_left[1])

	# if b upper intersects vertically
	if b_upper_left[1] >= a_lower_left[1] and b_upper_left[1] <= a_upper_left[1]:
		vertical_intersection_point_one = max(b_lower_left[1], a_lower_left[1])
		vertical_intersection_point_two = b_upper_left[1]

	if min(vertical_intersection_point_one, horizontal_intersection_point_one) != -1:
		return (vertical_intersection_point_two - vertical_intersection_point_one) * (horizontal_intersection_point_two - horizontal_intersection_point_one)
	else:
		return 0


my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 6,
    'height': 3,

}


my_rectangle2 = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 5,
    'height': 2,

}

print(intersection(my_rectangle, my_rectangle2))
