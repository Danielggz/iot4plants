from sense_hat import SenseHat
sense = SenseHat()

#display text
sense.show_message("Hello world!")

#colour set up
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)


#display text with colours
sense.show_message("Hello world again", text_colour=magenta, back_colour=cyan)

#uncomment out the lines below to see them in action 

#display text changing scroll speed
#sense.show_message("And slowly...Hello ", scroll_speed=0.2, text_colour=yellow, back_colour=blue)
#sense.show_message("World!", scroll_speed=0.5, text_colour=blue, back_colour=yellow)

#stops colours
sense.clear()
