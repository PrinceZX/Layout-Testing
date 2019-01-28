@objects
	s4titleh2-*      css    .padding-left-fit-container h2 p
	s4titlep		 css	.padding-left-fit-container .component-content > p:nth-child(2)
	view			 css    [href='https\:\/\/www\.google\.com\/']
	office-*	     css	[data-slides-per-view] .swiper-wrapper div:nth-of-type(1) [data-background-src] div p
	Retail-*	     css	.swiper-slide-visible [data-background-src='\/-\/media\/Project\/TECOM\/Media\/DIC\/Carousel\/Bounce\/wall-02\.jpg\?h\=1800\&w\=2880\&hash\=B5A3FE2A9147A420A7F97B7247A8B1E36C9FDA19'] div p
	ware-*		     css	.--big [data-background-src] div p
	arrow-*		     css	[data-slides-per-view] .swiper-controller div
	
= Slider 4 =	
	@on desktop
		s4titleh2-1:
                height ~70px
                width ~264px
                css font-size is "72px"
                aligned vertically left s4titleh2-2
                above s4titleh2-2 0 to ~5px
		 
		s4titleh2-2:   
				height ~70px
                width ~264px
                css font-size is "72px"
                near s4titlep ~30px top
                
        s4titlep:
        		height ~88px
        		width ~250px
 		
= Image Parts =      
	@on desktop 	 
        office-2:   
				height ~36px
                width ~85px
                css font-size is "30px"
                
        Retail-2:
        		height ~36px
                width ~78px
                css font-size is "30px"
                
        ware-2:   
				height ~36px
                width ~85px
                css font-size is "30px"

= Arrow Navigation = 
	@on desktop
		arrow-1:
				height ~19px
				width ~10px
				
		arrow-2:
				height ~19px
				width ~10px 	
                
= View All Products =
 	@on desktop	
 		view:
 				height ~22px
 				width ~151px              