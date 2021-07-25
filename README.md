A PLAYGROUND WHERE I TAKE A READY MADE WORDCLOUD LIBRARY AND MAKE IT HARD TO USE IT

I can't think of a way to accomodate all possible input formats that could be used as mask sources, so it doesn't make sense to invent
a list on my own, even a list that would include the mask samples found in this repo (that sample is in no way restricted... anything could be used in place of its elements and it should still work).
The and result should be in the form: "white is going to be removed (and if transparency is there probably setting it to 0 would be wise)",
this means that a png with seemingly proper values could have wrong rgb values even if the transparency us set correctly, it needs to be white.

about getting colors from the mask file:
save the file in a proper common format (e.g. png 24-bit), seriously it's not worth it to deal with this programmatically
