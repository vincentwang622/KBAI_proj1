# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
#import numpy
import random

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.

    def Solve(self,problem):
        #test. This will test each options
        #give score on each option
        def testAnswer(potentialAnswer):
            if potentialAnswer == oneValues:
                print  1
                return 1
            elif potentialAnswer == twoValues:
                print 2
                return 2
            elif potentialAnswer == threeValues:
                print 3
                return 3
            elif potentialAnswer == fourValues:
                print 4
                return 4
            elif potentialAnswer == fiveValues:
                print 5
                return 5
            elif potentialAnswer == sixValues:
                print 6
                return 6
            else:
                #compare which resembles most
                print 0
                return random.randint(0,6)
            
        #find out the mapping pattern between A and B's object
        def mappingPattern(a, b, c): # a,b,c is AValue, BValue, CValue
            #identical mapping
            mappings = []
            weight = 0
            if a == b:
               mappings.append('identical')
               weight += 5
               return mappings, weight
            

            #elif a == c:
                #mappings.append('reflection')
                #weight += 4
                #return mappings, weight

            else:
                #find difference B to A
                diffList = list(set(b.items()) - set(a.items()))
                diff = []
                for diffAttribute in diffList:
                    diffAttributeList = list(diffAttribute)
                    for diffAtt in diffAttributeList:
                        diff.append(diffAtt)
                #find reduced items A to B
                #reducedList = list(set(AFrame['a'].items()) - set(BFrame['b'].items()))
                    
                while diff:  
                    if 'angle' in diff: 
                        mappings.append('rotation')
                        weight += 3
                        diff.remove('angle')
                    if 'fill' in diff:
                        mappings.append('fill')
                        diff.remove('fill')
                    if 'size' in diff:
                        mappings.append('size')
                        diff.remove('size')
                    if 'shape' in diff:
                        mappings.append('shape')
                        diff.remove('shape')
                    if 'alignment' in diff:
                        mappings.append('alignment')
                        diff.remove('alignment')
                    else:
                        diff.pop()
                return  mappings, weight
            
        def generateDObject(mappings, i):
        #generate potential answer
            while mappings:
                if 'identical' in mappings:
                    if AValues[i] == BValues[i]:
                        DValues[i] = CValues[i]
                    elif AValues[i] == CValues[i]:
                        DValues[i] = BValues[i]
                    mappings.remove('identical')
                    
                #if 'reflection' in mappings:
                    #mappings.remove('reflection')
                    #DValues[i] = BValues[i]

                if 'rotation' in mappings:
                    AAngle = int(AValues[i].get('angle',0))
                    BAngle = int(BValues[i].get('angle',0))
                    CAngle = int(CValues[i].get('angle',0))
                    angleDiff = BAngle - AAngle
                    DAngle = CAngle - angleDiff
                    if 'angle' in DValues[i] and 'angle' in BValues[i]:
                        DValues[i]['angle'] = str(DAngle)
                    mappings.remove('rotation')

                if 'fill' in mappings:
                    AFill = AValues[i].get('fill')
                    BFill = BValues[i].get('fill')
                    CFill = CValues[i].get('fill')
                    DFill = ''
                    if AFill == 'yes' and BFill == 'no' and CFill == 'yes':
                        DFill = 'no'
                    elif AFill == 'no' and BFill == 'yes' and CFill == 'no':
                        DFill = 'yes'
                    DValues[i]['fill'] = DFill
                    mappings.remove('fill')
                    
                if 'size' in mappings:
                    #sizeList = ['huge', 'very large', 'large', 'medium','small', 'very small']
                    ASize = AValues[i].get('size')
                    BSize = BValues[i].get('size')
                    CSize = CValues[i].get('size')
                    DSize = ''
                    if ASize == CSize:
                        DSize = BSize
                    DValues[i]['size'] = DSize
                    mappings.remove('size')
                    
                if 'shape' in mappings:
                    AShape = AValues[i].get('shape')
                    BShape = BValues[i].get('shape')
                    CShape = CValues[i].get('shape')
                    DShape = ''
                    if AShape == CShape:
                        DShape = BShape
                    elif AShape == BShape:
                        DShape = CShape
                    DValues[i]['shape'] = DShape
                    mappings.remove('shape')

                if 'alignment' in mappings:
                    AAlignment = AValues[i].get('alignment')
                    BAlignment = BValues[i].get('alignment')
                    CAlignment = CValues[i].get('alignment')
                    DAlignment = ''
                    if AAlignment == 'bottom-right' and BAlignment == 'bottom-left' and CAlignment == 'top-right':
                        DAlignment = 'top-left'
                    elif AAlignment == 'top-left' and BAlignment == 'top-right' and CAlignment == 'bottom-left':
                        DAlignment = 'bottom-right'
                    DValues[i]['alignment'] = DAlignment
                    mappings.remove('alignment')

                #return 0
        #program start
        #retrieve value from the file
        A = problem.figures['A']
        B = problem.figures['B']
        C = problem.figures['C']
        solutionOne = problem.figures['1']
        solutionTwo = problem.figures['2']
        solutionThree = problem.figures['3']
        solutionFour = problem.figures['4']
        solutionFive = problem.figures['5']
        solutionSix = problem.figures['6']
        #figures = [A, B, C, solutionOne, solutionTwo, solutionThree, solutionFour, solutionFive, solutionSix]
        
        #create dictionaries for the frames 
        AFrame = {}
        BFrame = {}
        CFrame = {}
        DFrame = {}
        one = {}
        two = {}
        three = {}
        four = {}
        five = {}
        six = {}
        #frameList = [AFrame, BFrame, CFrame, DFrame, one, two, three, four, five, six]
        potentialAnswer = {}
        
        #build frame buildFrame()     
                
        for obj in list(A.objects):
            AFrame[A.objects[obj].name] = A.objects[obj].attributes
            
        for obj in list(B.objects):
            BFrame[B.objects[obj].name] = B.objects[obj].attributes

        for obj in list(C.objects):
            CFrame[C.objects[obj].name] = C.objects[obj].attributes
        
        for obj in list(solutionOne.objects):
            one[solutionOne.objects[obj].name] = solutionOne.objects[obj].attributes

        for obj in list(solutionTwo.objects):
            two[solutionTwo.objects[obj].name] = solutionTwo.objects[obj].attributes

        for obj in list(solutionThree.objects):
            three[solutionThree.objects[obj].name] = solutionThree.objects[obj].attributes

        for obj in list(solutionFour.objects):
            four[solutionFour.objects[obj].name] = solutionFour.objects[obj].attributes

        for obj in list(solutionFive.objects):
            five[solutionFive.objects[obj].name] = solutionFive.objects[obj].attributes

        for obj in list(solutionSix.objects):
            six[solutionSix.objects[obj].name] = solutionSix.objects[obj].attributes

        for obj in list(C.objects):
            DFrame[C.objects[obj].name] = C.objects[obj].attributes
        
        oneValues = sorted(one.values())
        twoValues = sorted(two.values())
        threeValues = sorted(three.values())
        fourValues = sorted(four.values())
        fiveValues = sorted(five.values())
        sixValues = sorted(six.values())
        AValues = sorted(AFrame.values())
        BValues = sorted(BFrame.values())
        CValues = sorted(CFrame.values())
        DValues = sorted(CFrame.values())
        valuesList = [AValues, BValues, CValues, oneValues, twoValues, threeValues, fourValues, fiveValues, sixValues]
        #relationship mapping from A to B 
        #mappings = []
        # one to one relationship
        if len(AValues) == 1 and len(BValues) == 1:
            mappingsH = mappingPattern(AValues[0], BValues[0],CValues[0])
            mappingsV = mappingPattern(AValues[0], CValues[0],BValues[0])
            if mappingsH[1]>=mappingsV[1]:
                generateDObject(mappingsH[0],0)
            else:
                DValues = sorted(BFrame.values())                
                generateDObject(mappingsV[0],0)
                
            potentialAnswer = DValues
            
        #multiple to multiple relationship
        else: 
            #delete 'inside' attribute
            for values in valuesList:
                for i in range(len(values)):
                    if 'inside' in values[i]:
                        del values[i]['inside']
                    if 'above' in values[i]:
                        del values[i]['above']
                            
            if len(AValues) == 2 and len(BValues) == 2: 

                A1, A2 = AValues[0], AValues[1]
                B1, B2 = BValues[0], BValues[1]
                C1, C2 = CValues[0], CValues[1]
    
                if A1 and B1 and C1:
                    mappings1 = mappingPattern(A1, B1, C1) 
                    generateDObject(mappings1[0],0)
                if A2 and B2 and C2:
                    mappings2 = mappingPattern(A2, B2, C2)
                    generateDObject(mappings2[0],1)
    
                potentialAnswer = DValues
                
            elif len(AValues) > len(BValues):            
                #detemine which object is deleted
                dltList = [AValue for AValue in AValues if AValue not in BValues]

                for dlt in dltList:
                    for DValue in DValues:
                        if dlt == DValue:
                            DValues.remove(DValue)
                potentialAnswer = DValues
        
        answer = testAnswer(potentialAnswer)
        return answer
        
        #if mappings == '':
            #return 0
        
