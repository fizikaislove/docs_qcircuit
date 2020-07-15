Transmon qubit
==========================
.. figure:: figures/Transmon_qubit.png
   :align: center
   :width: 4in


The transmon qubit can be described in charge basis by the Hamiltonian

.. math::
   H=4E_\text{C}(\hat{n}-n_g)^2+\frac{1}{2}E_\text{J}\sum_n(|n\rangle\langle n+1|+\text{h.c.}),

and in phase basis by

.. math::
   H=4E_\text{C}(\hat{n}-n_g)^2+\frac{1}{2}E_\text{J}\sum_n(|n\rangle\langle n+1|+\text{h.c.}),



Defining circuit topology
---------------------------------------------------------------

The circuit construction::

   Transmon = qubit.Circuit()
   Transmon.add_element(qubit.JosephsonJunction('JJ1'), ['GND', '1'])
   Transmon.add_element(qubit.JosephsonJunction('JJ2'), ['1', '2'])
   Transmon.add_element(qubit.Capacitance('Cq'), ['GND', '1'])

 give