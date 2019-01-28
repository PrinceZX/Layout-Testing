@objects
	header				  css       .wrap-top
	header-list-p-*		  css       .wrap-top .container a
	header-img-*		  css		.wrap-top .container a img
	logo-*			 	  css       .wrap-bottom .container a
	menu-item-*			  css		.wrap-bottom .container .primary .cta-primary 
	search		          css 		.ico-search
	menubtn				  css		[type='button']
		
= Header =
    @on desktop
     header:
            			inside screen 0px top
            			centered horizontally inside screen 1px
            			height 58 to 62px
 
= Header List With Images and Buttons =
	@on desktop
	= Explore button =
	 header-list-p-1:
						height ~ 34px
						width 249 to 253px
						text is "Explore Our Communities"
						near header-img-1 428px left
    
    = In5 Image =					
	 header-img-1:  
						height ~ 22px
						width 12px
						near header-img-3 50px left
	
	= Axs Image =					
	 header-img-3:  
						height ~ 13px
						width 39px	
						near header-list-p-4 20px left  					
	
	= Directory =
	 header-list-p-4:  
						height ~ 16px
						width 62px
						near header-list-p-5 20px left
						text is "Directory"
	
	= Setup button =					
     header-list-p-5:  
						height ~ 34px
						width 198 to 200px	
						text is "Set up your Business"

= Menu =
	@on desktop
  	 logo-1:
          				below header-list-p-1 43 to 45px
          				height 25px
          				width 186px
          				near menu-item-1 171px left
          				inside screen 80px left
	
	@on mobile, tablet
	 logo-1:
          				height 43px
          				width 80px
 
= Menu Items =	
	@on desktop 
	= Discover =
	 menu-item-1:
          				height ~ 16px
          				width 65px
          				css font-size is "14px"
          				text is "Discover"
          				near menu-item-2 ~ 40px left
    
    = Our Spaces =     
     menu-item-2:
          				height ~ 16px
          				width 76px
          				css font-size is "14px"
          				text is "Our Spaces"
          				near  menu-item-3 ~ 40px left
    
    = The Community =      
     menu-item-3:
          				height ~ 16px
          				width ~ 106px
          				css font-size is "14px"
          				text is "The Community"
          				near menu-item-4 ~ 40px left
    
    = Venues =				           				
     menu-item-4:
          				height ~ 16px
          				width 49px
          				css font-size is "14px"
          				text is "Venues"
          				near menu-item-5 ~ 40px left
    
    = Media =				         
     menu-item-5:
          				height ~ 16px
          				width ~ 41px
          				css font-size is "14px"
          				text is "Media"
          				near menu-item-6 ~ 40px left
    
    = Connect =				
     menu-item-6:
          				height ~ 16px
          				width ~ 56px
          				css font-size is "14px"
          				text is "Connect"
          				          				         			
= Search btn =    
    @on * 
     search:		    
     					height ~ 25px
	 					width 25px
	 					
= Menu btn = 	 					
	@on *				
	 menubtn:	        
	 					height ~ 11px
	 					width 25px	
	 							
	 
	