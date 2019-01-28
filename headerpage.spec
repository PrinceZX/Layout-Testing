@objects   
    header-list-*			 css     .wrap-top .comp-navbar a
	header-img-*		     css     .wrap-top .comp-navbar a img
	axs                      css     .wrap-top .comp-navbar-item:nth-of-type(3) [alt='Axs']:nth-of-type(1)
	
= Header =
    @on *
        header-list-1:
						height ~ 34px
						width 251px
						css font-size is "14px"
    			   		text is "Explore Our Communities "
    					
		header-img-1:  
						height ~ 22px
						width 12px
						near axs 50px left
						near header-list-1 428px right
						
		axs:  
						height ~ 13px
						width 39px	 					
		
		header-list-4:  
						height ~ 16px
						width 62px
						
		header-list-5:  
						height ~ 34px
						width 198px			
							
= Header Logo =
   @on desktop
	    mainlogo:          	
						height ~ 25px
          				width 186px

          				
     @on mobile, tablet
		footer-copy-p:
					height 18px
      				width 230px
      				css font-size is "9px"
   					css color is "#000000"
   					css font-family is "SFCompactText"
   					inside footer 20px left
   					inside footer 70px right
   					
   		footer-copy-li-1:
   					height 18px
      				width 75px
      				css font-size is "9px"
   					css color is "#000000"
   					css font-family is "SFCompactText"
   					
   		footer-copy-li-2:
   					height 18px
      				width 95px
      				css font-size is "9px"
   					css color is "#000000"
   					css font-family is "SFCompactText"
   					
   		footer-copy-li-3:
   					height 18px
      				width 60px
      				css font-size is "9px"
   					css color is "#000000"
   					css font-family is "SFCompactText"
   											