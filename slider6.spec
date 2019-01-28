@objects
	s6titleh2-*      css    .--right-image .field-promotext p
	s6titlep		 css	.--right-image .field-promotext2 p
	img				 css    [alt='a']
	get  		     css	.field-promolink [data-variantitemid='\{53AF6A85-55E3-460A-AEE4-AEA1209B18BC\}']

= Slider 6 =	
	@on desktop
		s6titleh2-1:
                height ~72px
                width ~534px
                css font-size is "72px"
 		
		s6titleh2-2:
                height ~72px
                width ~534px
                css font-size is "72px"
                inside screen 250px left
		 		 		
		s6titlep:   
				height ~110px
                width ~250px
       
        img:
        		height ~340px
        		width ~765px
        		inside screen 515px left
        		near s6titlep-1 15px right
        		
        get:
        		height ~22px
        		width ~99px
        		near img 166px left
        		near s6titlep 30px bottom
        		
      
                