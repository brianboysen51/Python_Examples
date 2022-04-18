#Q1 - 

import test
test.testEqual( mySum([2,3,1]),6)
test.testEqual( mySum([]),0)
test.testEqual( mySum([2]),2)
test.testEqual( mySum([-1,-2]),-3)
test.testEqual( mySum([0]),0)

#Q1.2 - C/D
#Q1.3 - A
#Q2 - 
import test
val=Student("Ananya",2)
test.testEqual( val.name,'Ananya')
test.testEqual(val.years_UM,2) #the passed value is not set rather the default value is set
test.testEqual(val.knowledge,0) 
test.testEqual(val.study(),None)
test.testEqual(val.year_at_umich(),2) #problem in year_at_umich because it will always return default value
test.testEqual(val.getKnowledge(),0) #problem in getKnowledge method
val=Student("Ananya")
test.testEqual(val.years_UM,1)

#Q2.2 - C/D
#Q2.3 - A



