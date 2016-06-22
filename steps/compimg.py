#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
image comparision module
depend:
<sudo apt-get install python-opencv>
options:
[sudo apt-get install python-numpy]
'''

__version__ = "2.0.1"
__author__ = "bhb"
__all__ = ['isMatch', 'getMatchedCenterOffset']

import os
try:
    import cv2
except ImportError, e:
    print e

def isMatch(subPath, srcPath, threshold=0.01):
    '''
    check wether the subPath image exists in the srcPath image.
    @type subPath: string
    @params subPath: the path of searched template. It must be not greater than the source image and have the same data type.
    @type srcPath: string
    @params srcPath: the path of the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        subImg = cv2.imread(subPath) #Load the sub image
        srcImg = cv2.imread(srcPath) #Load the src image
        result = cv2.matchTemplate(subImg, srcImg, method) #comparision
        minVal = cv2.minMaxLoc(result)[0] #Get the minimum squared difference
        if minVal <= threshold: #Compared with the expected similarity
            return True
        else:
            return False
    except:
        return False
    
def getMatchedCenterOffset(subPath, srcPath, threshold=0.01, rotation=0):
    '''
    get the coordinate of the mathced sub image center point.
    @type subPath: string
    @params subPath: the path of searched template. It must be not greater than the source image and have the same data type.
    @type srcPath: string
    @params srcPath: the path of the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference.
                       default is 0.01.
    @type rotation: int
    @params rotation: the degree of rotation. default is closewise. must be oone of 0, 90, 180, 270
    @rtype: tuple
    @return: (x, y) the coordniate tuple of the matched sub image center point. return None if sub image not found or any exception.
    '''
    for img in [subPath, srcPath]: assert os.path.exists(img) , "No such image:  %s" % (img)
    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        subImg = cv2.imread(subPath) #Load the sub image
        srcImg = cv2.imread(srcPath) #Load the src image
        result = cv2.matchTemplate(subImg, srcImg, method) #comparision
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result) #Get the minimum squared difference
        if minVal <= threshold: #Compared with the expected similarity
            minLocXPoint, minLocYPoint = minLoc
            subImgRow, subImgColumn = subImg.shape[:2]
            print subImg.shape
            centerPoint = (minLocXPoint + int(subImgRow/2), minLocYPoint + int(subImgColumn/2))
            #if image is binary format shape return (w, h) else return (w, h, d)
            (height, width) = srcImg.shape[:2]

            return adaptRotation(coord=centerPoint, size=(height, width), rotation=rotation)
        else:
            return None    
    except:
        return None

def adaptRotation(coord, size, rotation=0):
    if rotation == 0:
        return coord
    elif rotation == 90:
        height, width = size
        x_coord, y_coord = coord
        x = y_coord
        y = width - x_coord
        return (x, y)
    elif rotation == 180:
        height, width = size
        x_coord, y_coord = coord
        x = x_coord
        y = y_coord       
        return (x, y)
    elif rotation == 270:
        height, width = size
        x_coord, y_coord = coord
        x = height - y_coord
        y = x_coord
        return (x, y)
    else:
        return None
# *-* Kemin Added: Beginning *-*
def _isLImageMatch(subImg, srcImg, threshold=0.01):
    '''
    check wether the subImage image ~=/== the srcImage image.
    @type subImage: LoadImage
    @params subImage: the searched template. It must be not greater than the source image and have the same data type.
    @type srcImage: LoadImage
    @params srcImage: the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    method = cv2.cv.CV_TM_SQDIFF_NORMED #CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
    try:
        W, H = cv2.cv.GetSize(srcImg)
        w, h = cv2.cv.GetSize(subImg)
        width = W-w+1
        height = H-h+1
        result = cv2.cv.CreateImage((width,height), 32, 1)
        cv2.cv.MatchTemplate(srcImg, subImg, result, method)
        
        (minVal,maxVal,minLoc,maxLoc)=cv2.cv.MinMaxLoc(result)
        #print (minVal,maxVal,minLoc,maxLoc)
        if minVal <= threshold: #Compared with the expected similarity
            return True
        else:
            return False
    except Exception, e:
        print Exception, e
        return False
        
# to fix the pure black comparing's failure
def _inverse(image):
    size = (image.width,image.height)
    iTmp = cv2.cv.CreateImage(size,image.depth,image.nChannels)
    for i in range(image.height):
        for j in range(image.width):
            iTmp[i,j] = (255-image[i,j][0],255-image[i,j][1],255-image[i,j][2])
    return iTmp
        
def __isRectMatch(subImg, srcImg, threshold=0.01, rect=None):
    '''
    check wether the subImage's rectangle area ~=/== the srcImage's rectangle area.
    @type subImg: LoadImage
    @params subImg: the searched template. It must be not greater than the source image and have the same data type.
    @type srcImg: LoadImage
    @params srcImg: the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    try:
        if not rect:
            W, H = cv2.cv.GetSize(srcImg)
            rect = (0, 0, W, H)
        cv2.cv.SetImageROI(subImg, rect)
        subImg_rect = cv2.cv.CloneImage(subImg)
        cv2.cv.ResetImageROI(subImg)
        cv2.cv.SetImageROI(srcImg, rect)
        srcImg_rect = cv2.cv.CloneImage(srcImg)
        cv2.cv.ResetImageROI(srcImg) 
        return _isLImageMatch(subImg_rect, srcImg_rect, threshold)
    except Exception, e:
        print Exception, e
        return False
        
def isRectsMatch(subPath, srcPath, threshold=0.01, rects=None, isAll=True):
    '''
    check wether the subImage image's rectangle area ~=/== the srcImage image's rectangle area.
    @type subImage: LoadImage
    @params subImage: the searched template. It must be not greater than the source image and have the same data type.
    @type srcImage: LoadImage
    @params srcImage: the source image where the search is running.
    @type threshold: float
    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
    @type rects: Rect
    @params rects: the compared rectangle area list.
    @type isAll: Boolean
    @params isAll: ture, all rects should be lower than threshold => return true. false, any rect is lower than threshold => return true.
    @rtype: boolean
    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
    '''
    # 1. validate the sub and src path
    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
    try:
        srcImg = cv2.cv.LoadImage(srcPath) #Load the src image
        subImg = cv2.cv.LoadImage(subPath) #Load the sub image
        inverse_sub = _inverse(subImg)
        inverse_src = _inverse(srcImg)
    except Exception, e:
        print Exception, e
        return False
    
    # 2.1 if not specify the rect, compare the whole image
    if rects == None:
        return __isRectMatch(subImg, srcImg, threshold, rect=None)
        
    # 2.2 if specify the rect, compare rect one by one
    result = []
    try:
        for r in rects:
            result_orig = __isRectMatch(subImg, srcImg, threshold, rect=tuple(r))
            result_inv = __isRectMatch(inverse_sub, inverse_src, threshold, rect=tuple(r))
            res = (result_orig, result_inv)
            result.append(any(res))
            print r, result
    except Exception, e:
        print Exception, e
        return False
    
    if isAll:
        return all(result)
    else:
        return any(result)
# *-* Kemin Added: End *-*
    
def debug():
    #print _isRectMatch2(subPath=r'/home/ckt/labofkm/images/mypic.png', srcPath=r'/home/ckt/labofkm/images/mypic2.png')
    import time
    t1=time.time()
    print isRectsMatch(subPath=r'/home/ckt/labofkm/images/mypic.png', srcPath=r'/home/ckt/labofkm/images/mypic2.png', threshold=0.1, rects=[(965,10,99,48),(819,453,254,189),(360,728,90,154),(639,1048,81,152),(636,1360,81,152),(909,1400,74,66)], isAll=True)
    t2=time.time()
    print t2-t1
    
#test method
if __name__ == '__main__':
    debug()
    
    
# ==================================================
# not used now
#def isPartMatch(subPath, srcPath, threshold=0.01, rect=None):
#    '''
#    check wether the subPath image's rectangle area part exists in the srcPath image.
#    @type subPath: string
#    @params subPath: the path of searched template. It must be not greater than the source image and have the same data type.
#    @type srcPath: string
#    @params srcPath: the path of the source image where the search is running.
#    @type threshold: float
#    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
#    @rtype: boolean
#    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
#    '''
#    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
#    method = cv2.cv.CV_TM_SQDIFF_NORMED #Parameter specifying the comparison method 
#    try:
#        srcImg = cv2.cv.LoadImage(srcPath) #Load the src image
#        W, H = cv2.cv.GetSize(srcImg)
#        if not rect:
#            rect = (0, 0, W, H)
#            
#        subImg = cv2.cv.LoadImage(subPath) #Load the sub image
#        cv2.cv.SetImageROI(subImg, rect)
#        subImg_rect = cv2.cv.CloneImage(subImg)
#        cv2.cv.ResetImageROI(subImg)
#        
#        w, h = cv2.cv.GetSize(subImg_rect)
#        width = W-w+1
#        height = H-h+1
#        result = cv2.cv.CreateImage((width,height), 32, 1)
#        cv2.cv.MatchTemplate(srcImg, subImg_rect, result, method)
#        
#        (minVal,maxVal,minLoc,maxLoc)=cv2.cv.MinMaxLoc(result)
#        if minVal <= threshold: #Compared with the expected similarity
#            return True
#        else:
#            return False
#    except Exception, e:
#        print Exception, e
#        return False

## debug function
#def f1():
#    subImg = cv2.cv.LoadImage('red.png')
#    srcImg = cv2.cv.LoadImage('red2.png')
#    print _isLImageMatch(subImg, srcImg, threshold=0.01)

#def _check_against_origin_inverse(subImg, srcImg, threshold=0.01):
#    origin_sub = subImg
#    origin_src = srcImg
#    inverse_sub = _inverse(subImg)
#    inverse_src = _inverse(srcImg)
#    print "threshold"
#    th = threshold
#    
#    result_orig = _isLImageMatch(origin_sub, origin_src, threshold=th)
#    result_inv = _isLImageMatch(inverse_sub, inverse_src, threshold=th)
#    result = (result_orig, result_inv)
#    return any(result)

#def isRectMatch(subPath, srcPath, threshold=0.01, rect=None):
#    '''
#    check wether the subImage image's rectangle area ~=/== the srcImage image's rectangle area.
#    @type subImage: LoadImage
#    @params subImage: the searched template. It must be not greater than the source image and have the same data type.
#    @type srcImage: LoadImage
#    @params srcImage: the source image where the search is running.
#    @type threshold: float
#    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
#    @rtype: boolean
#    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
#    '''
#    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
#    try:
#        srcImg = cv2.cv.LoadImage(srcPath) #Load the src image
#        W, H = cv2.cv.GetSize(srcImg)
#        if not rect:
#            rect = (0, 0, W, H)
#        subImg = cv2.cv.LoadImage(subPath) #Load the sub image
#        
#        # origin
#        cv2.cv.SetImageROI(subImg, rect)
#        subImg_rect = cv2.cv.CloneImage(subImg)
#        cv2.cv.ResetImageROI(subImg)
#        cv2.cv.SetImageROI(srcImg, rect)
#        srcImg_rect = cv2.cv.CloneImage(srcImg)
#        cv2.cv.ResetImageROI(srcImg)
#        #return _isLImageMatch(subImg_rect, srcImg_rect, threshold=0.01)
#        #return _check_against_origin_inverse(subImg_rect, srcImg_rect, threshold=0.01)
#        result_orig = _isLImageMatch(subImg_rect, srcImg_rect, threshold)
#        
#        # inverse
#        inverse_sub = _inverse(subImg)
#        inverse_src = _inverse(srcImg)
#        cv2.cv.SetImageROI(inverse_sub, rect)
#        inverse_subImg_rect = cv2.cv.CloneImage(inverse_sub)
#        cv2.cv.ResetImageROI(inverse_sub)
#        cv2.cv.SetImageROI(inverse_src, rect)
#        inverse_srcImg_rect = cv2.cv.CloneImage(inverse_src)
#        cv2.cv.ResetImageROI(inverse_src)
#        result_inv = _isLImageMatch(inverse_subImg_rect, inverse_srcImg_rect, threshold)
#        
#        result = (result_orig, result_inv)
#        return any(result)
#    except Exception, e:
#        print Exception, e
#        return False
#        
#def isRectsMatch(subPath, srcPath, threshold=0.01, rects=None, isAll=True):
#    '''
#    check wether the subImage image's rectangle area ~=/== the srcImage image's rectangle area.
#    @type subImage: LoadImage
#    @params subImage: the searched template. It must be not greater than the source image and have the same data type.
#    @type srcImage: LoadImage
#    @params srcImage: the source image where the search is running.
#    @type threshold: float
#    @params threshold: the minixum value which used to increase or decrease the matching threshold. 0.01 means at most 1% difference. default is 0.01. 
#    @type rects: Rect
#    @params rects: the compared rectangle area list.
#    @type isAll: Boolean
#    @params isAll: ture, all rects should be lower than threshold => return true. false, any rect is lower than threshold => return true.
#    @rtype: boolean
#    @return: true if the sub image founded in the src image. return false if sub image not found or any exception.
#    '''
#    for img in [subPath, srcPath]: assert os.path.exists(img) , 'No such image:  %s' % (img)
#    # if not specify the rect, compare the whole image
#    if rects == None:
#        return isRectMatch(subPath, srcPath, threshold, rect=None)
#    # if specify the rect, compare rect one by one
#    result = []
#    try:
#        for r in rects:
#            res = isRectMatch(subPath, srcPath, threshold, rect=tuple(r))
#            result.append(res)
#            #print r, res
#    except Exception, e:
#        print Exception, e
#        return False
#    
#    if isAll:
#        return all(result)
#    else:
#        return any(result)

#def debug():
#    #print isMatch(subPath='sub1.png', srcPath='full1.png', threshold=0.1)
#    #print getMatchCenterOffset(subPath='sub1.png', srcPath='full1.png', threshold=0.01)
#    #print download("http://ats.borqs.com/smartserver/static/img/logo-s.png")
#    #print isMatch(subPath='red.png', srcPath='red2.png', threshold=0.1)
#    #print isRectMatch(subPath='red.png', srcPath='red2.png', threshold=0.1, rect=(0, 0, 50, 50))
#    #print isRectMatch(subPath='black.png', srcPath='red.png', threshold=0.1)
#    #print isRectMatch(subPath='black.png', srcPath='red.png', threshold=0.1, rect=(0, 0, 50, 50))
#    #print isRectMatch(subPath='black.png', srcPath='red_black.png', threshold=0.1, rect=(0, 0, 50, 50))
#    #print isRectMatch(subPath='white2.png', srcPath='red_white.png', threshold=0.1, rect=(0, 0, 50, 50))
#    #print isRectMatch(subPath='red.png', srcPath='red_white.png', threshold=0.1, rect=(0, 0, 50, 50))
#    #print isPartMatch(subPath='desert.jpg', srcPath='desert2.jpg', threshold=0.1, rect=(200, 200, 100, 100))
#    #f1()
#    #print isRectMatch(subPath='red.png', srcPath='red_white.png', threshold=0.1, rect=(200, 200, 300, 300))
#    #print isRectsMatch(subPath='red.png', srcPath='red_white.png', threshold=0.1, 
#    #rects=[(0, 0, 50, 50), (500, 200, 200, 300), (200, 200, 300, 300)], isAll=True)
#    print isRectsMatch(subPath='red.png', srcPath='red_white.png', threshold=0.1, 
#    rects=[(0, 0, 50, 50), (500, 200, 200, 300), (85, 380, 500, 500)], isAll=True)
#    
#def debug2():
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/red.png', srcPath=r'/home/ckt/labofkm/images/red_white.png', threshold=0.1)
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/red.png', srcPath=r'/home/ckt/labofkm/images/red2.png', threshold=0.1)
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black.png', srcPath=r'/home/ckt/labofkm/images/black2.png', threshold=0.1)
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black.png', srcPath=r'/home/ckt/labofkm/images/black2.png', threshold=0.1)
#    
#def debug3():
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white2.png', threshold=0.1)
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1)
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white2.png', threshold=0.1, rect=(45, 45, 100, 100))
#    print isRectMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1, rect=(45, 45, 100, 100))
#
#def debug4():
#    print isRectsMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white2.png', threshold=0.1, rects=[(45, 45, 100, 100), (50, 50, 60, 60), (50, 50, 90, 90)], isAll=True)
#    print isRectsMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1, rects=[(45, 45, 100, 100), (50, 50, 60, 60), (50, 50, 90, 90)], isAll=True)
#    print isRectsMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1, rects=[(45, 45, 100, 100), (50, 50, 60, 60), (50, 155, 30, 30)], isAll=True)
#    
#def debug5():
#    import time
#    t1=time.time()
#    print isRectsMatch(subPath=r'/home/ckt/labofkm/images/mypic.png', srcPath=r'/home/ckt/labofkm/images/mypic2.png', threshold=0.1, rects=[(965,10,99,48),(819,453,254,189),(360,728,90,154),(639,1048,81,152),(636,1360,81,152),(909,1400,74,66)], isAll=True)
#    t2=time.time()
#    print t2-t1
#    #print isRectsMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1, rects=[(965,10,99,48),(819,453,254,189),(360,728,90,154),(639,1048,81,152),(636,1360,81,152),(909,1400,74,66)], isAll=True)
#    #print isRectsMatch(subPath=r'/home/ckt/labofkm/images/black2.png', srcPath=r'/home/ckt/labofkm/images/white_black2.png', threshold=0.1, rects=[(965,10,99,48),(819,453,254,189),(360,728,90,154),(639,1048,81,152),(636,1360,81,152),(909,1400,74,66)], isAll=True)
