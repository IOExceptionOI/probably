r"""
---
AST
---

All data types to represent a pGCL program.

.. note::

    For our AST types, most "sum types" have a normal Python superclass (e.g. :class:`TypeClass` for types), but also a Union type (e.g. :data:`Type`).
    **Prefer using the Union type, as it allows for exhaustiveness checking by mypy.**

    In some rare cases, it's necessary to tell mypy that an object of a superclass type is actually in the respective union.
    Use ``cast`` methods, e.g. :meth:`InstrClass.cast` to go from :class:`InstrClass` to :data:`Instr`.

    Also note that ``isinstance`` checks must be done against the superclasses, because Python's Union does not yet work with ``isinstance``.

Program
#######
.. autoclass:: Program

    .. automethod:: __str__

Types
#####
.. autodata:: Type
.. autoclass:: BoolType
.. autoclass:: NatType
.. autoclass:: Bounds
.. autoclass:: RealType

Declarations
############
.. autodata:: Decl
.. autoclass:: VarDecl
.. autoclass:: ConstDecl
.. autoclass:: ParameterDecl


.. _expressions:

Expressions
###########

In the AST, a bunch of different things that look like program expressions are
lumped together. Formally, let a state :math:`\sigma \in \Sigma` consists of a
bunch of values for each variable, and be represented by a function of type
:math:`\sigma : \text{Var} \to \text{Value}`.

First, there are *state expressions* that, given a state :math:`\sigma`, compute
some value to be used later in the program itself: :math:`\Sigma \to
\text{Value}`. There are two types of expressions we call *monadic expressions*:
:class:`UniformExpr` and :class:`CategoricalExpr`. They map a state to a
distribution of values: :math:`\Sigma \to \text{Dist}[\Sigma]`. And
*expectations* are also expressed using :data:`Expr`, but they are actually a
mapping of states to *expected values*: :math:`\Sigma \to \mathbb{R}`.

.. autodata:: Expr
.. autodata:: DistrExpr
.. autoclass:: VarExpr
.. autoclass:: BoolLitExpr
.. autoclass:: NatLitExpr
.. autoclass:: RealLitExpr
.. autoclass:: Unop
.. autoclass:: UnopExpr
.. autoclass:: Binop
.. autoclass:: BinopExpr
.. autoclass:: DUniformExpr
.. autoclass:: CUniformExpr
.. autoclass:: BernoulliExpr
.. autoclass:: GeometricExpr
.. autoclass:: PoissonExpr
.. autoclass:: LogDistExpr
.. autoclass:: BinomialExpr
.. autoclass:: IidSampleExpr
.. autoclass:: CategoricalExpr
.. autoclass:: SubstExpr
.. autoclass:: TickExpr

Instructions
############
.. autodata:: Instr
.. autodata:: Query
.. autoclass:: SkipInstr
.. autoclass:: WhileInstr
.. autoclass:: IfInstr
.. autoclass:: AsgnInstr
.. autoclass:: ChoiceInstr
.. autoclass:: LoopInstr
.. autoclass:: TickInstr
.. autoclass:: ObserveInstr
.. autoclass:: ExpectationInstr
.. autoclass:: OptimizationType
.. autoclass:: OptimizationQuery
.. autoclass:: ProbabilityQueryInstr
.. autoclass:: PrintInstr
.. autoclass:: PlotInstr

Superclasses
############
These are only used for use with isinstance.
Otherwise use corresponding Union types instead.

.. autoclass:: TypeClass
.. autoclass:: DeclClass

    .. automethod:: __str__

.. autoclass:: ExprClass

    .. automethod:: __str__

.. autoclass:: InstrClass

    .. automethod:: __str__

.. autoclass:: Node
"""

from .ast import Node, Var
from .declarations import DeclClass, ConstDecl, Decl, ParameterDecl, VarDecl
from .expressions import (FunctionCallExpr,BernoulliExpr, BinomialExpr, Binop, BinopExpr,
                          BoolLitExpr, CategoricalExpr, CUniformExpr,
                          DistrExpr, DUniformExpr, Expr, ExprClass,
                          GeometricExpr, IidSampleExpr, LogDistExpr,
                          NatLitExpr, PoissonExpr, RealLitExpr, SubstExpr,
                          TickExpr, Unop, UnopExpr, VarExpr, expr_str_parens)
from .instructions import (sample_predefined_functions,AbortInstr, QueryInstr,AsgnInstr, ChoiceInstr, ExpectationInstr, IfInstr,
                           Instr, InstrClass, LoopInstr, ObserveInstr,
                           OptimizationQuery, OptimizationType, PlotInstr,
                           PrintInstr, ProbabilityQueryInstr, Query, SkipInstr,
                           TickInstr, WhileInstr)
from .program import Program
from .types import TypeClass, BoolType, Bounds, NatType, RealType, Type
from .walk import *
