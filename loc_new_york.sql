SELECT E1.ENAME,E1.SAL,E2.ENAME,D2.DNAME
FROM EMP E1,EMP E2,DEPT D2
WHERE E1.MGR=E2.EMPNO AND 
E2.DEPTNO = D2.DEPTNO AND D2.LOC='NEW YORK' AND E2.SAL>3000;

