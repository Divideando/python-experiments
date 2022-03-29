
def encontradoNumble (strOut):
    print ("Encontrado numble")
    print (strOut)

def solveNumble (objetivo, nums, strOut):
    if len(nums) < 2: 
        return None
    for i in range(0, len(nums)-1):
        for j in range(i+1,len(nums)):
            # array de números sin los dos que vamos operar
            aTmp = []
            for k in range(0,len(nums)):
                if (k!=i) and (k!=j) :
                    aTmp.append(nums[k])
            # Suma, no importa orden
            strAux = str(nums[i])+'+'+str(nums[j])+'='+str(nums[i]+nums[j])+"\n"
            if ((nums[i] + nums[j]) == objetivo):
                encontradoNumble (strOut+strAux)
                exit (0)
            aFunc = aTmp.copy()
            aFunc.append(nums[i] + nums[j])
            solveNumble(objetivo, aFunc, strOut+strAux)
            # Resta, sólo si no da negativo
            if ((nums[i] - nums[j]) > 0) :
                resta = nums[i] - nums[j]
                strAux = str(nums[i])+'-'+str(nums[j])+'='+str(resta)+"\n"
            else :
                resta = nums[j] - nums[i]
                strAux = str(nums[j])+'-'+str(nums[i])+'='+str(resta)+"\n"
            if (resta == objetivo):
                encontradoNumble (strOut+strAux)
                exit (0)
            aFunc = aTmp.copy()
            aFunc.append(resta)
            solveNumble(objetivo, aFunc, strOut+strAux)
            # Multiplicación
            strAux = str(nums[i])+'*'+str(nums[j])+'='+str(nums[i]*nums[j])+"\n"
            if ((nums[i] + nums[j]) == objetivo):
                encontradoNumble (strOut+strAux)
                exit (0)
            aFunc = aTmp.copy()
            aFunc.append(nums[i] * nums[j])
            solveNumble(objetivo, aFunc, strOut+strAux)
            # Division, sólo si es exacta y el divisor no es cero
            if (nums[j] != 0) and ((nums[i] % nums[j]) == 0) :
                strAux = str(nums[i])+'/'+str(nums[j])+'='+str(nums[i]/nums[j])+"\n"
                if ((nums[i] / nums[j]) == objetivo):
                    encontradoNumble (strOut+strAux)
                    exit (0)
                aFunc = aTmp.copy()
                aFunc.append(nums[i] / nums[j])
                solveNumble(objetivo, aFunc, strOut+strAux)
            if (nums[i] != 0) and ((nums[j] % nums[i]) == 0) :
                strAux = str(nums[j])+'/'+str(nums[i])+'='+str(nums[j]/nums[i])+"\n"
                if ((nums[j] / nums[i]) == objetivo):
                    encontradoNumble (strOut+strAux)
                    exit (0)
                aFunc = aTmp.copy()
                aFunc.append(nums[j] / nums[i])
                solveNumble(objetivo, aFunc, strOut+strAux)


solveNumble(843, [1,2,3,7,75,100], "")
