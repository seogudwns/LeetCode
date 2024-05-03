class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1,version2 = [int(i) for i in version1.split('.')],[int(i) for i in version2.split('.')]
        
        minleng,a,b = min(len(version1),len(version2)),1,-1
        if len(version1)<len(version2):
            version1,version2,a,b = version2,version1,b,a
            
        for i in range(minleng):
            if version1[i]>version2[i]:
                return a
            elif version1[i]<version2[i]:
                return b
        
        if len(version1)>minleng:
            for i in range(minleng,len(version1)):
                if version1[i]>0:
                    return a
        return 0
            
        