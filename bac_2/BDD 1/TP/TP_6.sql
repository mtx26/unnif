select *  from dept d where not exists (select * from emp e where d.deptno = e.deptno);
//ou 
select deptno from dept except select deptno from emp;


select *  from dept d where not exists (select * from emp e where d.deptno = e.deptno and e.job
= 'ANALYST');

select ename, sal from emp e
where (select COUNT(*) from emp m where m.sal > e.sal) < 3
ORDER by sal DESC;
//ou
select ename, sal from emp e ORDER by sal DESC limit 3;