SELECT E1.ENAME,E1.SAL,E2.ENAME,E2.SAL,D1.DNAME
FROM EMP E1,EMP E2,DEPT D1
WHERE E1.MGR=E2.EMPNO AND
E1.DEPTNO=D1.DEPTNO AND E1.SAL>E2.SAL;
