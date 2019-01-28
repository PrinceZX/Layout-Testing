@objects
	s5titleh2        css    .comp-quote h2
	s5titlep-*		 css	.comp-quote [data-swiper-slide-index='0']:nth-of-type(2) .quote-item p
	author			 css    .comp-quote [data-swiper-slide-index='0']:nth-of-type(2) .quote-item span
	img			     css	.comp-quote [data-swiper-slide-index='0']:nth-of-type(2) .quote-item img
	aview 		     xpath	//div[@class='swiper-wrapper']/div[2]//a[@title='View']
	
= Slider 5 =	
	@on desktop
		s5titleh2:
                height ~ 141px
                width ~298px
                css font-size is "72px"
                near s5titlep-1 ~30px top
		 
		s5titlep-1:   
				height ~158px
                width ~529px
                css font-size is "30px"
        		near author ~20px top
        		
        author:
        		height ~16px
        		width ~62px
        		css font-size is "14px"
        		near s5titlep-2 ~17px top 
        		
        s5titlep-2:   
				height ~22px
                width ~184px
                css font-size is "14px"		
        
        img:
        		height ~61px
        		width ~60px
        		near s5titlep-2 ~266px right		      
        		
        aview:
        		height ~22px
        		width ~50px