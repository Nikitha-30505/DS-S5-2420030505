#longest common subsequence
def lcs_length(X,Y):
    m,n=len(X), len(Y)

    #create a matrix to store lengths of LCS
    dp=[[0]*(n+1) for _ in range(m+1)]

    #build the matrix
    for i in range(m):
        for j in range(n):
            if X[i]==Y[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

#ex
s1="ABCDEF"
s2="AEBDF"
length=lcs_length(s1,s2)
print(f"Longest Common Subsequence length between '{s1}' and '{s2}' : {length}")