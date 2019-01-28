@objects
	logo				  css	 [title] .img-light [alt]
	search				  css	 [data-toggle]
	menu-hide			  css	 .icon-menu

= logo Image =
	@on desktop
		 logo:
		 		height 25px
		 		width 186px			
          						  
    @on mobile,tablet
    	 logo: 
    			height 43px
    			width 280px 		
		
		
		 = Menu =
    @on desktop
  	 menu-list-1:
          				width 186px
	 					height ~ 25px
	 					below header-list-p-1 10 to 43px
	 					near menu-list-2 171px left
          				
     menu-list-2:
          				height ~ 16px
          				width 65px
          				css font-size is "14px"
          				text is "Discover"
          				near menu-list-8 40px left
         
     menu-list-8:
          				height ~ 16px
          				width 76px
          				css font-size is "14px"
          				text is "Our Spaces"
          				near menu-list-21 40px left
          
     menu-list-21:
          				height ~ 16px
          				width 106px
          				css font-size is "14px"
          				text is "The Community"
          				near menu-list-26 40px left
    				           				
     menu-list-26:
          				height ~ 16px
          				width 49px
          				css font-size is "14px"
          				text is "Venues"
          				near menu-list-33 40px left
    				         
     menu-list-33:
          				height ~ 16px
          				width 41px
          				css font-size is "14px"
          				text is "Media"
          				near menu-list-36 40px left
    				
     menu-list-36:
          				height ~ 16px
          				width 56px
          				css font-size is "14px"
          				text is "Connect"
          				near menu-list-40 60px left
          				
     menu-list-40:
          				height 25px
	 					width 25px
	 					below header-list-p-3 10 to 43px
	 					near menu-list-40 60px right	
	 					
	 						
	Silder 3 					
	 announce-*   css	[class='item-col col-xs-12 col-md-4'] .category
	busine-p-*	 css	[class='item-col col-xs-12 col-md-4'] .business-park
	title-*		 css	[class='item-col col-xs-12 col-md-4'] .title
	desc-*	     css	[class='item-col col-xs-12 col-md-4'] .desc
						
						
						= Announce =
	@on desktop
		announce-1:
		  		width 120px
		  		height 16px
		  		near announce-2 221px left
		  		
		announce-2:
		  		width 120px
		  		height 16px
		  		near announce-3 221px left
		  		
		announce-3:
		  		width 120px
		  		height 16px
		  				  		
		announce-4:
		  		width 120px
		  		height 16px
		  		below announce-1 10 to 248px
		  		 		  		
		announce-5:
		  		width 120px
		  		height 16px
		  		near announce-6 221px left
		  		below announce-2 10 to 248px
		  		
		announce-6:
		  		width 120px
		  		height 16px
		  		below announce-3 10 to 248px 
		 
= Business =	
	@on desktop
		busine-p-1:
		  		width 120px
		  		height 14px
		  		
		busine-p-2:
		  		width 120px
		  		height 14px
		  		 		
		busine-p-3:
		  		width 120px
		  		height 14px
		  		
		busine-p-4:
		  		width 120px
		  		height 14px
		
		busine-p-5:
		  		width 120px
		  		height 14px
		
		busine-p-6:
		  		width 120px
		  		height 14px
		  		
= Title =
	@on desktop
		title-1:
		  		width 140px
		  		height 70px
		  		
		title-2:
		  		width 140px
		  		height 70px
		  		 		
		title-3:
		  		width 140px
		  		height 70px
		  		
		title-4:
		  		width 140px
		  		height 70px
		
		title-5:
		  		width 140px
		  		height 70px
		
		title-6:
		  		width 140px
		  		height 70px
		  		
= Details =
	@on desktop
		desc-1:
		  		width 210px
		  		height 90px
		  		
		desc-2:
		  		width 210px
		  		height 90px
		  		 		
		desc-3:
		  		width 210px
		  		height 90px
		  		
		desc-4:
		  		width 210px
		  		height 90px
		
		desc-5:
		  		width 210px
		  		height 90px
		
		desc-6:
		  		width 210px
		  		height 90px
		  		
	--=-==-=-=	  		
	= Footer Copyright =
    @on desktop
     	footer-copy-p:
     				height 18px
      				width 230px
      				css font-size is "9px"
   					css color is "#000000"
   					css font-family is "SFCompactText"
   					inside footer 80px left
   					inside footer 970px right 				
      	      				
      	  		
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
      								
   -=-=-=-=-=-=-=-
   
   
   footer-list-3:
      			    height ~ 29px
      			    width ~ 119px
      				near footer-list-4 10px top
      				near footer-list-5 105px left
      				aligned horizontally all footer-list-4
      	
		footer-list-4:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-6
      				
      	footer-list-5:
      				height ~ 14px
      				width ~ 54px
      				near footer-list-6 10px top
      				near footer-list-1 150px left
      				aligned horizontally all footer-list-7
      		
      	footer-list-6:
      			    height ~ 14px
      			    width ~ 115px
      				near footer-list-7 10px top
      				near footer-list-2 109px left
      				aligned horizontally all footer-list-8
      				
        footer-list-7:
      			    height ~ 29px
      			    width ~ 119px
      				near footer-list-8 10px top
      				near footer-list-3 105px left
      				aligned horizontally all footer-list-9
      	
		footer-list-8:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-4 60px left
      				aligned horizontally all footer-lists-5
      				
      	footer-list-9:
      				height ~ 14px
      				width ~ 54px
      				near footer-list-10 10px top
      				near footer-list-5 150px left
      				aligned horizontally all footer-list-10
      		
      	footer-list-10:
      			    height ~ 14px
      			    width ~ 115px
      				near footer-list-11 10px top
      				near footer-list-6 109px left
      				aligned horizontally all footer-list-11
      				
        footer-list-11:
      			    height ~ 29px
      			    width ~ 119px
      				near footer-list-12 10px top
      				near footer-list-5 105px left
      				aligned horizontally all footer-list-12
      	
		footer-list-12:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-9
      				
      	footer-list-13:
      				height ~ 14px
      				width ~ 54px
      				near footer-list-14 10px top
      				near footer-list-5 150px left
      				aligned horizontally all footer-list-14
      		
      	footer-list-14:
      			    height ~ 14px
      			    width ~ 115px
      				near footer-list-15 10px top
      				near footer-list-6 109px left
      				aligned horizontally all footer-list-15
      				
        footer-list-15:
      			    height ~ 29px
      			    width ~ 119px
      				near footer-list-4 10px top
      				near footer-list-5 105px left
      				aligned horizontally all footer-list-16
      	
		footer-list-16:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-13		
      				
      	footer-list-17:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-2 10px top
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-18		
      
      	footer-list-18:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-2 10px top
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-19			
      		
      	footer-list-19:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-2 10px top
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-20			
      
      	footer-list-20:
      			    height ~ 14px
      			    width ~ 64px
      				near footer-list-5 60px left
      				aligned horizontally all footer-list-17			
      				
= footer copyright = 
		
		 							   	 
      	  		