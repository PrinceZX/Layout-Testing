function scroll() 
{
	driver.executeScript("javascript:window.scrollBy(0,350)");
	
	var screenshotFile = takeScreenshot(driver);
	
		test("Some basic test", function ()
		{
		  // ...
		  this.report.error("Something went wrong on the page")
	      .withAttachment("Screenshot", takeScreenshot(driver));
		});
	
	var browsers =
	{
	   firefox:
	   {
		   browserName: "Firefox"
	   },
	   chrome:
	   {
		   browserName: "Chrome"
   	   },
	   ie:
	   {
		   browserName: "Internet Explorer"
	   }
	};

	forAll(forAll(browsers, function ()
		{
		    test("Test on ", function (browser)
		    	{
			      // some test code
			    });
	    }); 
    });
}