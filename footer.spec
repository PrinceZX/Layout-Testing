@objects
	  footer-stay			   css     .footer-newsletter h2
	  footer-p				   css     .footer-newsletter p
	  footer-email			   css     .comp-input [type]
	  footer-drp			   css     .choices__list--single [data-id]
	  footer-button            xapth   //button[@class='cta-primary']
	  footer-h3-*			   css     .container-flex .component-content h3		
	  footer-copy-p			   css     .footer-copyright p
	  footer-copy-li-*		   css     .footer-copyright .container > .component-content li
	  
= Footer = 
    @on desktop
   		footer-stay:
   					height 141px
   					width 283px
   					inside footer 250px left
   					inside footer 747px right
   					inside footer 492px bottom
   					css font-size is "72px"
   					text is "Stay in touch"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					above footer-p 10 to 30px
   					
   		footer-p:
   					height 22px
   					width 250px
   					css font-size is "16px"
   					text is "Sign up for our Newsletter."
   					css color is "#414042"
   					css font-family is "SFCompactText"
   					inside footer 250px left
   					inside footer 440px bottom
   					inside footer 780px right
   					below footer-stay 10 to 30px
   					
   		footer-email:
   					width 303px
   					css font-size is "20px"
   					text is "Email"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					css background-color is "white"
   					
   		footer-drp:
   					width 303px
   					css font-size is "20px"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					css background-color is "white"
   					
   	    footer-button:
   	   			    width 71px
   	   			    height 22px

= mobile view =   	
   	@on mobile, tablet
   		footer-stay:
   					height 81px
   					width 280px
   					inside footer 20px left
   					inside footer 20px right
   					css font-size is "42px"
   					text is "Stay in touch"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					above footer-p 10 to 20px
   					
   		footer-p:
   					height 22px
   					width 280px
   					css font-size is "16px"
   					text is "Sign up for our Newsletter."
   					css color is "#414042"
   					css font-family is "SFCompactText"
   					inside footer 20px left
   					inside footer 20px right
   					below footer-stay 10 to 20px
   					
   		footer-email:
   					width 230px
   					css font-size is "16px"
   					text is "Email"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					css background-color is "white"
   					
   		footer-drp:
   					width 230px
   					css font-size is "16px"
   					css color is "#000000"
   					css font-family is "SFProDisplay"
   					css background-color is "white"
   					
   	    footer-button:
   	   			    width 57px
   	   			    height 22px
   	
= Footer list =   
    @on *
     	footer-h3-1:
     				height 22px
     				width 91px
     				near footer-h3-2 135px left
     				near footer-list-1 27px top
     				     				
     	footer-h3-2:
     				height 22px
     				width 73px
     				near footer-h3-3 135px left
     				near footer-list-5 27px top
     				
     	footer-h3-3:
     				height 22px
     				width 87px
     				near footer-h3-4 135px left
     				near footer-list-9 27px top
     				
     	footer-h3-4:
     				height 22px
     				width 74px
     				near footer-h3-5 135px left
     				near footer-list-13 27px top
     				
     	footer-h3-5:
     				height 22px
     				near footer-h3-4 135px right
     				near footer-list-17 27px top
     				
= Footer list navigation =     				
@import footer2.spec