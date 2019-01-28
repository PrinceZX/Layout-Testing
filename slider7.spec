@objects
	s6titleh2        css    .comp-social-media h2
	s6box			 css	.comp-social-media-container
	imgbox-*		 css    .comp-social-media-container div ul li
	explore		     css	[data-variantitemid='\{C70970A6-9466-444E-8FA3-10A78FBACD85\}']
	
= Slider 7 =	
	@on desktop
		s6titleh2:
                height ~141px
                width ~251px
                css font-size is "72px"
                inside screen ~250px left
		 		
		s6box:   
				height ~210px
                width ~810px
                inside screen ~235px left right
                near explore ~30px top
                
        imgbox-1:
        		height ~180px
        		width ~250px
        		inside s6box ~15px left top bottom
        
        imgbox-4:
        		height ~180px
        		width ~250px
        		inside s6box ~15px top bottom
        		near imgbox-1 ~15px right
        		
        imgbox-7:
        		height ~180px
        		width ~250px
        		inside s6box ~15px right top bottom
        		near imgbox-4 ~15px right 
        		
        explore:
        		height ~22px
        		width ~218px
        		css font-size is "20px"
        		
        		    
                