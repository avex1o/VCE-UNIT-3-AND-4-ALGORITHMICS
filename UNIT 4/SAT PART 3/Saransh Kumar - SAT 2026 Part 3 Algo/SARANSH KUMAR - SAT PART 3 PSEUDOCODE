Initialise Node, Edge, and Graph classes exactly as used in Part 2 solution
define Haversine function exactly as used in Part 2 solution

Function GenerateRoute(list, maxTime) # run this function on the "toMine" list
    route := []
    timeTaken : = 0
    unvisited := copy of list

    choose random node from unvisited to be starting node
    add node to route

    remove node from unvisited

    while unvisited is not empty and timeTaken < maxTime
        choose random unvisited neighbour

        if route time + neighbour total time <= maxTime

            add neighbour to route

            miningTime := get mining time of neighbour
            travelTime := get travel time to neighbour

            timeTaken := timeTaken + miningTime + travelTime 
        
        if else no unvisited neighbours
            return route 
        
        else
            return route 

Function evaluate(route)
    score := 0

    for each node in route 
        yield := get yield of node
        score := score + yield 

    return score


Function acceptanceProbability(inital, final, temp)
    probability := e^(-(final-inital)/temp)
    return probability



Algorithm FindRoute(nodes, maxTime, iterations, initialTemperature, decayRate)

    cache := empty dictionary

    currentRoute := GenerateRoute(nodes, maxTime)
    currentScore := Evaluate(currentRoute)

    cache[currentRoute] := currentScore

    bestRoute := currentRoute
    bestScore := currentScore

    temperature := initialTemperature

    for iteration in iterations

        newRoute := GenerateRoute(nodes, maxTime)

        if newRoute exists in cache then
            newScore := cache[newRoute]
        else
            newScore := Evaluate(newRoute)
            cache[newRoute] := newScore
        end if

        if newScore > currentScore then
            currentRoute := newRoute
            currentScore := newScore

        else
            acceptProb := acceptanceProbability(currentScore, newScore, temperature)
            randomProb := random float between 0 and 1

            if randomProb is less than acceptProb THEN
                currentRoute := newRoute
                currentScore := newScore
            end if
        end if

        if currentScore > bestScore THEN
            bestRoute := currentRoute
            bestScore := currentScore
        end if

        temperature := temperature * decayRate # if decay rate is 0.95 then temp will decrease by 5 percent

    end for

    return bestRoute, bestScore
End Algorithm