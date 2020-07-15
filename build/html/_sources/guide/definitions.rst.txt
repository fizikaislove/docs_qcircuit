The Hamiltonian parameter definitions
======================================
Here you can read an explanation of the Hamiltonian parameter definitions in the Circuit library.

.. math::
    E_{J}&=\frac{\hbar I_C}{2e} \text{  is a Josephson junction energy,}\\
    E_{C}&=\frac{e^2}{2C} \text{  is a charge energy,}\\
    E_{L}&=(\frac{\hbar}{2e})^2\frac{1}{2L} \text{  is an inductor energy,}\\
    \Phi_x &= 2\pi\frac{\Phi}{\Phi_0} = \frac{2e \Phi}{\hbar} \text{  is an external applied flux, in units of radians.}

To simplify these definitions, :math:`2e` and :math:`\hbar`` were equated to unity, giving:

.. math::
    &I_C=E_{J} \text{ Josephson junction critical current = Josephson junction energy}\\
    &С=\frac{1}{8 E_{C}} \text{  is a capacity,}\\
    &L=\frac{1}{2 E_{L}} \text{  is an inductance,}\\
    &\Phi_x = \Phi \text{  is an external applied flux, in units of radians}

Which means if you want to specify the Josephson junction energy you should set critical current in GHz.