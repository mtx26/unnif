select ename, deptno, sal from emp where (deptno, sal) in (select deptno, sal from emp where comm is not null);

select ename, hiredate, sal 
    from emp 
    where 
        (sal, ifnull(comm, -1)) = (
            select sal, ifnull(comm,-1) 
            from emp 
            where ename = 'SCOTT') 
        and not ename = 'SCOTT';

