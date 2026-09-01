# EEE 111 — Final Exam Solution Guide

### Recognize the Type → Pick the Formula → Solve

Covers **Chapter 4 (BJT DC Biasing)**, **Chapter 1 (Diode Equation)**, and **Chapter 2 (Diode Applications)**

Based on the questions in `EEE111_qestions.docx` — all 52 questions solved (28 from Chapter 4, 5 from Chapter 1, 19 from Chapter 2).

<div class="pagebreak"></div>

## How to Use This Guide

This guide follows the **same order as your question file**: Chapter 4 first, then Chapter 1, then Chapter 2.

**Study order that works best:**

1. Read **Part 1** for one chapter. Learn how to *recognize* each type.
2. Copy the formulas for that chapter from **Part 2** onto one page by hand.
3. Do the questions of that type from **Part 3**. Cover the solution first, try it yourself, then check.
4. The night before the exam, read only the **Final Exam Quick Revision** section.

**Constants used throughout:**

| Symbol | Value | Where used |
|---|---|---|
| V<sub>BE</sub> | 0.7 V | Silicon BJT, always |
| V<sub>K</sub> (Si) | 0.7 V | Silicon diode turn-on |
| V<sub>K</sub> (Ge) | 0.3 V | Germanium diode turn-on |
| V<sub>K</sub> (GaAs) | 1.2 V | GaAs diode turn-on |
| V<sub>K</sub> (Ideal) | 0 V | Ideal diode |
| k/q | 8.62 × 10<sup>−5</sup> V/K | Thermal voltage |

**Two things flagged in your document** (details inside — I did not invent values):

- Fig. 2.155(a): the first digit of the battery is cut off at the image edge. It does not change the answer.
- Ch. 1 Q16 and Q17: the `I_s` values are written in **mA**, which is very large for a reverse saturation current. Both answers are given.

<div class="pagebreak"></div>

# PART 1 — HOW TO RECOGNIZE AND SOLVE

# Chapter 4 — BJT DC Biasing

**Golden rule for the whole chapter:** every problem is solved by writing **KVL around the base–emitter loop first** to get I<sub>B</sub>, then I<sub>C</sub> = βI<sub>B</sub>, then **KVL around the collector–emitter loop** to get V<sub>CE</sub>.

Learn to spot the configuration by **what is connected to the base**.

| What you see at the base | Configuration |
|---|---|
| One resistor R<sub>B</sub> going to V<sub>CC</sub>, emitter grounded | Fixed bias |
| One resistor R<sub>B</sub> to V<sub>CC</sub>, **plus R<sub>E</sub>** at emitter | Emitter bias |
| **Two** resistors R<sub>1</sub>, R<sub>2</sub> forming a divider | Voltage-divider bias |
| R<sub>F</sub> going from base to the **collector** (not V<sub>CC</sub>) | Collector feedback |
| Output taken at emitter, no R<sub>C</sub> | Emitter follower |
| Base grounded / base at a fixed voltage, input at emitter | Common base |

---

### Type 1: Fixed-Bias — Find the Q-point

**How to recognize this type:**

- One single resistor R<sub>B</sub> from V<sub>CC</sub> to the base.
- The emitter goes **straight to ground** (no R<sub>E</sub>).
- Question asks for I<sub>BQ</sub>, I<sub>CQ</sub>, V<sub>CEQ</sub>, V<sub>C</sub>, V<sub>B</sub>, V<sub>E</sub>.

**What I need to find:**

- I<sub>B</sub>, then I<sub>C</sub>, then V<sub>CE</sub> and the three node voltages.

**Given information:**

- V<sub>CC</sub>, R<sub>B</sub>, R<sub>C</sub>, β.

**Formula:**

    I_B = (V_CC − 0.7) / R_B
    I_C = β × I_B
    V_CE = V_CC − I_C × R_C
    V_C = V_CE        V_E = 0 V        V_B = 0.7 V

- V<sub>CC</sub> = supply voltage (V), R<sub>B</sub> = base resistor (Ω), R<sub>C</sub> = collector resistor (Ω), β = current gain (no unit).

**How to solve:**

1. Write I<sub>B</sub> = (V<sub>CC</sub> − 0.7) / R<sub>B</sub>. Answer will be in **µA**.
2. Multiply by β to get I<sub>C</sub>. Answer will be in **mA**.
3. V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub>.
4. Because the emitter is grounded: V<sub>E</sub> = 0, so V<sub>C</sub> = V<sub>CE</sub> and V<sub>B</sub> = 0.7 V.

**Quick exam trick:**
> **No R<sub>E</sub> → fixed bias.** Only R<sub>B</sub> matters for I<sub>B</sub>. V<sub>C</sub> = V<sub>CE</sub> and V<sub>B</sub> = 0.7 V for free.

---

### Type 2: Emitter-Bias — Find the Q-point

**How to recognize this type:**

- One resistor R<sub>B</sub> from V<sub>CC</sub> to base, **and** a resistor R<sub>E</sub> between the emitter and ground.
- Words like "emitter-stabilized bias circuit".

**What I need to find:**

- I<sub>B</sub>, I<sub>C</sub>, I<sub>E</sub>, V<sub>E</sub>, V<sub>C</sub>, V<sub>CE</sub>, V<sub>B</sub>.

**Given information:**

- V<sub>CC</sub>, R<sub>B</sub>, R<sub>C</sub>, R<sub>E</sub>, β.

**Formula:**

    I_B = (V_CC − 0.7) / (R_B + (β + 1) R_E)      ← the key formula
    I_C = β I_B          I_E = (β + 1) I_B
    V_E = I_E × R_E
    V_C = V_CC − I_C × R_C
    V_CE = V_C − V_E
    V_B = V_E + 0.7

**How to solve:**

1. Use the big denominator: R<sub>B</sub> + (β+1)R<sub>E</sub>. **This is the step people forget.**
2. Get I<sub>C</sub> and I<sub>E</sub>.
3. V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> (use I<sub>E</sub>, not I<sub>C</sub>).
4. V<sub>C</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub> (use I<sub>C</sub>, not I<sub>E</sub>).
5. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub>, and V<sub>B</sub> = V<sub>E</sub> + 0.7.

**Quick exam trick:**
> **R<sub>E</sub> present → the emitter resistor gets multiplied by (β+1) when seen from the base.** That single change turns Type 1 into Type 2.

---

### Type 3: Voltage-Divider Bias — Find the Q-point

**How to recognize this type:**

- **Two** resistors R<sub>1</sub> (top) and R<sub>2</sub> (bottom) forming a divider at the base.
- Almost always an R<sub>E</sub> at the emitter too.

**What I need to find:**

- Same list: I<sub>B</sub>, I<sub>C</sub>, V<sub>CE</sub>, V<sub>C</sub>, V<sub>E</sub>, V<sub>B</sub>.

**Given information:**

- V<sub>CC</sub>, R<sub>1</sub>, R<sub>2</sub>, R<sub>C</sub>, R<sub>E</sub>, β.

**There are two methods. Check the condition first:**

    Condition (Eq. 4.33):   β R_E  ≥  10 R_2

**Formula — EXACT (Thévenin) method — always valid:**

    R_Th = R_1 R_2 / (R_1 + R_2)          (parallel)
    E_Th = V_CC × R_2 / (R_1 + R_2)       (divider)
    I_B  = (E_Th − 0.7) / (R_Th + (β + 1) R_E)
    I_C  = β I_B        I_E = (β + 1) I_B
    V_E  = I_E R_E      V_B = V_E + 0.7
    V_C  = V_CC − I_C R_C
    V_CE = V_C − V_E

**Formula — APPROXIMATE method — only if βR<sub>E</sub> ≥ 10R<sub>2</sub>:**

    V_B  = V_CC × R_2 / (R_1 + R_2)       (ignore I_B completely)
    V_E  = V_B − 0.7
    I_E  = V_E / R_E         and    I_C ≈ I_E
    V_CE = V_CC − I_C (R_C + R_E)
    I_B  = I_C / β

**How to solve:**

1. Test βR<sub>E</sub> ≥ 10R<sub>2</sub>. If the question says "use the approximate approach", just check and state it.
2. If using exact: find R<sub>Th</sub> and E<sub>Th</sub> first, then treat it exactly like Type 2.
3. If using approximate: no I<sub>B</sub> at all in the divider — read V<sub>B</sub> straight off the divider.
4. Finish with V<sub>C</sub>, V<sub>E</sub>, V<sub>CE</sub>.

**Quick exam trick:**
> **Two base resistors → Thévenin.** Approximate = "pretend I<sub>B</sub> = 0". Exact = "replace the divider with R<sub>Th</sub> and E<sub>Th</sub>, then it is emitter bias".

---

### Type 4: Collector-Feedback (Voltage-Feedback) Bias

**How to recognize this type:**

- The base resistor R<sub>F</sub> connects the base to the **collector node**, not to V<sub>CC</sub>.
- Words: "collector-feedback", "voltage feedback network".
- If two resistors sit in series in that feedback path with a capacitor to ground between them, **add them** (a capacitor is an open circuit for DC).

**What I need to find:**

- I<sub>B</sub>, I<sub>C</sub>, V<sub>C</sub>, and sometimes V<sub>E</sub>, V<sub>CE</sub>.

**Given information:**

- V<sub>CC</sub>, R<sub>F</sub>, R<sub>C</sub>, R<sub>E</sub> (may be 0), β.

**Formula:**

    I_B = (V_CC − 0.7) / (R_F + β (R_C + R_E))     ← note: β, not (β+1)
    I_C = β I_B
    V_C = V_CC − I_C R_C
    V_E = I_C R_E
    V_CE = V_C − V_E

**How to solve:**

1. Add up any series feedback resistors (capacitors → open).
2. Put R<sub>C</sub> + R<sub>E</sub> inside the bracket, multiplied by β.
3. Get I<sub>C</sub>, then the node voltages.

**Quick exam trick:**
> **R<sub>F</sub> touches the collector → the denominator is R<sub>F</sub> + β(R<sub>C</sub>+R<sub>E</sub>).** Compare with emitter bias, where it was R<sub>B</sub> + (β+1)R<sub>E</sub>.

---

### Type 5: Emitter-Follower

**How to recognize this type:**

- Output is taken at the **emitter**.
- The collector connects **directly to V<sub>CC</sub>** with no R<sub>C</sub>.
- Often a split supply (+V at top, −V at bottom).

**What I need to find:**

- I<sub>B</sub>, I<sub>E</sub>, V<sub>E</sub>, and sometimes V<sub>BC</sub>, V<sub>CE</sub>.

**Given information:**

- Supply(s), R<sub>B</sub> (or R<sub>1</sub>, R<sub>2</sub>), R<sub>E</sub>, β.

**Formula:**

    Single base resistor with split supply (+V and −V):
    I_B = (V_top + |V_bottom| − 0.7) / (R_B + (β + 1) R_E)
    I_E = (β + 1) I_B
    V_E = −|V_bottom| + I_E R_E

    Divider version: find R_Th, E_Th first, then
    I_B = (E_Th − 0.7) / (R_Th + (β + 1) R_E)
    V_E = I_E R_E       V_C = V_CC      V_CE = V_C − V_E     V_BC = V_B − V_C

**How to solve:**

1. Walk the base–emitter loop, adding up **both** supplies if the bottom rail is negative.
2. Same denominator as emitter bias: R<sub>B</sub> + (β+1)R<sub>E</sub>.
3. V<sub>E</sub> is measured from the **bottom rail**, so add the negative supply back in.
4. V<sub>C</sub> = V<sub>CC</sub> always (no R<sub>C</sub> to drop voltage).

**Quick exam trick:**
> **No R<sub>C</sub> → V<sub>C</sub> = V<sub>CC</sub>.** With a −6 V rail and +6 V rail, the driving voltage is 6 + 6 − 0.7 = 11.3 V.

---

### Type 6: Common-Base

**How to recognize this type:**

- The **base is grounded** or held at a fixed DC voltage.
- The input signal goes into the **emitter**.
- The transistor is often drawn lying on its side.

**What I need to find:**

- I<sub>E</sub> first (not I<sub>B</sub>), then I<sub>C</sub>, then V<sub>C</sub> and V<sub>CE</sub>.

**Given information:**

- Emitter supply, R<sub>E</sub>, collector supply, R<sub>C</sub>, sometimes β or a fixed V<sub>B</sub>.

**Formula:**

    V_E = V_B − 0.7                (V_B = 0 if base grounded)
    I_E = (V_E − V_EE) / R_E       (V_EE = the emitter-side supply)
    I_B = I_E / (β + 1)            I_C = β I_B ≈ I_E
    V_C = V_CC − I_C R_C
    V_CE = V_C − V_E               V_BC = V_B − V_C

**How to solve:**

1. Find V<sub>E</sub> from the base voltage: V<sub>E</sub> = V<sub>B</sub> − 0.7.
2. Apply Ohm's law across R<sub>E</sub> between V<sub>E</sub> and the emitter supply to get I<sub>E</sub>.
3. If β is given, split into I<sub>B</sub> and I<sub>C</sub>. If not, use I<sub>C</sub> ≈ I<sub>E</sub>.
4. Get V<sub>C</sub>, then subtract.

**Quick exam trick:**
> **Base grounded → V<sub>E</sub> = −0.7 V.** Then everything comes from Ohm's law. Start at the emitter, not the base.

---

### Type 7: Saturation Current (I<sub>Csat</sub>)

**How to recognize this type:**

- The words "saturation current" or "I<sub>Csat</sub>".
- Usually a one-line question referring back to an earlier figure.

**What I need to find:**

- The maximum possible collector current, when V<sub>CE</sub> is forced to 0.

**Given information:**

- V<sub>CC</sub> and whichever resistors are in the collector–emitter path.

**Formula:**

    Fixed bias (no R_E):        I_Csat = V_CC / R_C
    Any circuit with R_E:       I_Csat = V_CC / (R_C + R_E)

**How to solve:**

1. Short the transistor (imagine V<sub>CE</sub> = 0).
2. Add the resistances that remain in the collector-to-emitter path.
3. Divide V<sub>CC</sub> by that sum. **β is not used at all.**

**Quick exam trick:**
> **Saturation = short the transistor.** Just V<sub>CC</sub> ÷ (resistors in the C–E path). Takes 10 seconds — free marks.

---

### Type 8: "Reverse" Problems — Given Voltages, Find Resistors / β / V<sub>CC</sub>

**How to recognize this type:**

- The circuit has **letters instead of numbers** on some resistors (R<sub>B</sub>, R<sub>C</sub>, R<sub>1</sub>).
- Instead, node voltages or currents are printed on the figure (V<sub>C</sub> = 7.6 V, I<sub>B</sub> = 20 µA, I<sub>E</sub> = 4 mA).
- Wording: "Given the information appearing in Fig. …, determine …".

**What I need to find:**

- Whatever is missing: R<sub>B</sub>, R<sub>C</sub>, R<sub>E</sub>, R<sub>1</sub>, β, or V<sub>CC</sub>.

**Given information:**

- Read every number printed on the figure. Those are your knowns.

**Formula (rearranged versions of the normal ones):**

    R_C = (V_CC − V_C) / I_C            R_E = V_E / I_E
    R_B = (V_CC − V_B) / I_B            β  = I_C / I_B
    I_C = I_E − I_B                      V_B = V_E + 0.7
    V_CC = V_CE + I_C R_C + V_E
    For a divider:  I_2 = V_B / R_2 ,  I_1 = I_2 + I_B ,  R_1 = (V_CC − V_B) / I_1

**How to solve:**

1. List every value printed on the figure.
2. Find a resistor that has **both** its end voltages and its current known — solve that one first.
3. Use V<sub>B</sub> = V<sub>E</sub> + 0.7 to unlock the base side.
4. Keep going; each answer unlocks the next.

**Quick exam trick:**
> **Same formulas, just rearranged.** Always start from a resistor where you know voltage across it *and* current through it.
>
> **Careful with R<sub>1</sub>:** the current through R<sub>1</sub> is I<sub>2</sub> **+ I<sub>B</sub>**, not just I<sub>2</sub>.

---

### Type 9: Design Problems

**How to recognize this type:**

- The word "**Design**" or "**Determine R<sub>C</sub> and R<sub>B</sub> for…**".
- No figure at all — everything is in the text.
- Says "Use standard values".

**What I need to find:**

- Resistor values that produce the requested Q-point.

**Given information:**

- V<sub>CC</sub>, β, and the target I<sub>CQ</sub> and V<sub>CEQ</sub>.

**Formula:**

    R_C = (V_CC − V_CEQ − V_E) / I_CQ        (V_E = 0 if no R_E)
    R_E = V_E / I_E
    I_B = I_CQ / β
    R_B = (V_CC − 0.7 − V_E) / I_B
    Divider design:  R_2 ≤ β R_E / 10   then   R_1 = V_CC R_2 / V_B − R_2

**How to solve:**

1. Draw the circuit yourself from the description.
2. Work out every node voltage from the target Q-point.
3. Ohm's law on each resistor.
4. Round to the **nearest standard value** at the end (see the standard-value list in Part 2).

**Quick exam trick:**
> **Design = normal analysis run backwards.** Find the voltage across each resistor, divide by the current through it, then round.

---

### Type 10: Current-Source Circuits

**How to recognize this type:**

- Question says "**Calculate the current through the load**" or "calculate the current I".
- The current arrow **I** is drawn in the collector branch.
- May include a **Zener diode** setting the base voltage.

**What I need to find:**

- I, which is just I<sub>C</sub>.

**Given information:**

- Supplies, base network, R<sub>E</sub>, β.

**Formula:**

    Find V_B from whatever sets it:
       Fixed source through R_B   → use KVL with (β+1)R_E
       Resistor divider            → use R_Th / E_Th
       Zener                       → V_B = V_bottom + V_Z    (Zener fixes it directly)
    Then:
       V_E = V_B − 0.7
       I_E = (V_E − V_bottom) / R_E
       I = I_C = α I_E = β/(β+1) × I_E

**How to solve:**

1. Get V<sub>B</sub>. **This is the whole problem.**
2. Subtract 0.7 to get V<sub>E</sub>.
3. Ohm's law across R<sub>E</sub> gives I<sub>E</sub>.
4. I<sub>C</sub> is I<sub>E</sub> shaved by α = β/(β+1) — usually a 1% change.

**Quick exam trick:**
> **The load resistor value does not matter.** That is the whole point of a current source. If a question gives you a "2.2 kΩ load", it is a distractor — the current is set by the base and R<sub>E</sub>.

<div class="pagebreak"></div>

# Chapter 1 — Semiconductor Diodes (The Diode Equation)

**All five questions in this chapter use one equation and one constant.** There are no circuits.

---

### Type 1: Find the Thermal Voltage V<sub>T</sub>

**How to recognize this type:**

- "Determine the thermal voltage for a diode at a temperature of …".
- A temperature in °C is given.

**What I need to find:**

- V<sub>T</sub> in millivolts.

**Given information:**

- Temperature in °C.

**Formula:**

    T_K = T_C + 273
    V_T = k T_K / q          where k/q = 8.62 × 10^−5 V/K
    V_T = (8.62 × 10^−5) × T_K

- k = Boltzmann constant = 1.38 × 10<sup>−23</sup> J/K, q = 1.6 × 10<sup>−19</sup> C.

**How to solve:**

1. Convert °C to Kelvin by **adding 273**.
2. Multiply by 8.62 × 10<sup>−5</sup>.
3. Express in mV.

**Quick exam trick:**
> **Add 273, multiply by 8.62 × 10<sup>−5</sup>.** At room temperature (25 °C / 298 K) you should get ≈ 26 mV — use that as a sanity check.

---

### Type 2: Find the Diode Current I<sub>D</sub> (forward bias)

**How to recognize this type:**

- Gives I<sub>s</sub>, n, and a **positive** V<sub>D</sub>.
- Says "using Eq. 1.2" or "using the diode equation".

**What I need to find:**

- I<sub>D</sub> in mA.

**Given information:**

- I<sub>s</sub> (reverse saturation current), n (ideality factor, 1 or 2), V<sub>D</sub>, temperature.

**Formula:**

    I_D = I_s ( e^(V_D / (n V_T)) − 1 )         ← Shockley equation (Eq. 1.2)

- n = ideality factor (1 for high current, 2 for low current), V<sub>T</sub> = thermal voltage (V).

**How to solve:**

1. Get V<sub>T</sub> for the given temperature (Type 1).
2. Compute the exponent: V<sub>D</sub> ÷ (n × V<sub>T</sub>).
3. Take e to that power on your calculator.
4. Subtract 1, multiply by I<sub>s</sub>.

**Quick exam trick:**
> **n multiplies V<sub>T</sub>, not V<sub>D</sub>.** Writing V<sub>D</sub>/V<sub>T</sub> and forgetting n doubles the exponent and destroys the answer.

---

### Type 3: Diode Current under Reverse Bias

**How to recognize this type:**

- The applied voltage is **negative** ("reverse-bias potential of −10 V").
- Often followed by "Is the result expected? Why?".

**What I need to find:**

- I<sub>D</sub>, which will simply be −I<sub>s</sub>.

**Given information:**

- I<sub>s</sub>, n, negative V<sub>D</sub>.

**Formula:**

    I_D = I_s ( e^(V_D / (n V_T)) − 1 )
    For V_D negative and large:  e^(negative big) ≈ 0
    So   I_D ≈ I_s (0 − 1) = −I_s

**How to solve:**

1. Note the exponent is a large negative number.
2. e<sup>(large negative)</sup> ≈ 0.
3. So I<sub>D</sub> = −I<sub>s</sub>. Answer is the saturation current, flowing backwards.
4. For "is it expected?" — yes, a reverse-biased diode passes only its tiny leakage current.

**Quick exam trick:**
> **Reverse bias → the answer is just −I<sub>s</sub>.** No calculator needed.

---

### Type 4: Find I<sub>s</sub> (given I<sub>D</sub> and V<sub>D</sub>)

**How to recognize this type:**

- "Given a diode current of … find I<sub>s</sub>".

**What I need to find:**

- I<sub>s</sub>, usually in pA or nA.

**Given information:**

- I<sub>D</sub>, V<sub>D</sub>, n, temperature.

**Formula:**

    I_s = I_D / ( e^(V_D / (n V_T)) − 1 )

**How to solve:**

1. Find V<sub>T</sub> from the temperature.
2. Compute the exponential term.
3. Divide I<sub>D</sub> by (that term − 1).

**Quick exam trick:**
> **Same equation, divide instead of multiply.** Expect a very tiny answer (pA/nA) — if you get mA, you inverted it.

---

### Type 5: Find V<sub>D</sub> (given I<sub>D</sub> and I<sub>s</sub>)

**How to recognize this type:**

- "find the applied voltage V<sub>D</sub>".
- V<sub>T</sub> is often given directly (e.g. 26 mV) so you skip Type 1.

**What I need to find:**

- V<sub>D</sub> in volts — should land near 0.4–0.8 V.

**Given information:**

- I<sub>D</sub>, I<sub>s</sub>, n, V<sub>T</sub>.

**Formula:**

    V_D = n V_T × ln ( I_D / I_s + 1 )        ← natural log, not log₁₀

**How to solve:**

1. Divide I<sub>D</sub> by I<sub>s</sub> (watch the powers of ten — this is a huge number).
2. Add 1, take **ln**.
3. Multiply by n × V<sub>T</sub>.

**Quick exam trick:**
> **Rearranged Shockley = ln form.** Use **ln**, never log. Sanity check: the answer must be a sensible diode voltage, roughly 0.3–0.8 V.

<div class="pagebreak"></div>

# Chapter 2 — Diode Applications

**Golden rule for the whole chapter:** every DC diode problem is answered by first deciding **ON or OFF** for each diode.

**The universal test:**

1. **Assume the diode is OFF.** Remove it (open circuit) and find the voltage that would appear across it.
2. If the **anode is more positive** than the cathode by more than V<sub>K</sub>, it is really **ON**.
3. Redo the circuit with the diode replaced by a battery of V<sub>K</sub> (or a wire if ideal).
4. Check your assumption: the current must flow in the arrow's direction. If it comes out negative, the diode is OFF.

**Reading the symbol:** current flows in the direction the **triangle points**. The **bar** is the cathode (the negative/blocking side).

---

### Type 1: Series Diode Circuit — Find I, V<sub>o</sub>, I<sub>D</sub>

**How to recognize this type:**

- One loop with one or two diodes and resistors.
- "Determine the current I" / "Determine V<sub>o</sub> and I<sub>D</sub>".
- Diodes labelled Si, Ge, GaAs, or Ideal.

**What I need to find:**

- Whether each diode conducts, then the loop current and output voltage.

**Given information:**

- Supply voltages and their polarity, resistor values, diode material.

**Formula:**

    I = (Total driving voltage − Σ diode drops) / (Σ resistances)
    V_o = I × R_output          (or V_o = 0 if no current flows)
    Si → 0.7 V     Ge → 0.3 V     GaAs → 1.2 V     Ideal → 0 V

**How to solve:**

1. Mark the polarity of every source. **A battery with "−" on top makes that node negative.**
2. Check each diode's direction against the driving voltage.
3. If OFF → I = 0 and V<sub>o</sub> = 0 (no current, no drop across the resistor).
4. If ON → subtract every diode drop from the driving voltage, divide by the total resistance.

**Quick exam trick:**
> **Diode OFF → I = 0 → V<sub>o</sub> = 0 V.** Half of these questions are answered in one line. Always check the direction before doing any arithmetic.

---

### Type 2: Two Diodes Pointing at Each Other (Back-to-Back)

**How to recognize this type:**

- Two diodes in the **same branch** with the triangles pointing in **opposite** directions.
- Or one bar-then-triangle and one triangle-then-bar in series.

**What I need to find:**

- Nothing complicated — that branch is dead.

**Given information:**

- Just look at the two symbols.

**Formula:**

    Opposing diodes in series  →  branch is an OPEN CIRCUIT  →  I = 0

**How to solve:**

1. Spot the opposing pair.
2. Delete that whole branch from the circuit.
3. Solve whatever is left (usually a trivial resistor problem).

**Quick exam trick:**
> **Arrows facing each other = wire cut.** One diode always blocks, whichever way current tries to go.

---

### Type 3: Parallel Diode Branches (both may conduct)

**How to recognize this type:**

- Two branches, each with its own diode, joining at the same output node.
- Different diode materials (e.g. one Si, one GaAs) in the two branches.

**What I need to find:**

- V<sub>o</sub> at the common node, then the current in each branch.

**Given information:**

- Supply, both branch resistances, both diode types.

**Formula:**

    Assume both ON, write KCL at the output node:
    (V_supply − V_K1 − V_o)/R_1  +  (V_supply − V_K2 − V_o)/R_2  =  V_o / R_load
    Solve for V_o, then check each branch current is positive.

**How to solve:**

1. Assume both diodes conduct.
2. KCL at the output node: current in = current out.
3. Solve the single linear equation for V<sub>o</sub>.
4. **Check both branch currents are positive.** If one is negative, that diode is OFF — redo with only the other.

**Quick exam trick:**
> **Two diode branches meeting → KCL at the joint.** Do not assume the smaller-drop diode "wins" — with a resistor in each branch, both usually conduct.

---

### Type 4: Half-Wave Rectifier

**How to recognize this type:**

- One diode, sinusoidal input, "half-wave rectifier".
- Asks you to **sketch** v<sub>i</sub>, v<sub>d</sub>, i<sub>d</sub>, v<sub>L</sub>.

**What I need to find:**

- Peak value V<sub>m</sub>, the DC level, and the three waveforms.

**Given information:**

- Either V<sub>m</sub> or the DC level, the frequency, and R.

**Formula:**

    Ideal diode:     V_dc = 0.318 V_m           (0.318 = 1/π)
    Silicon diode:   V_dc = 0.318 (V_m − 0.7)
    Peak output:     V_o(peak) = V_m − V_K
    Peak current:    I_peak = (V_m − V_K) / R
    Period:          T = 1 / f
    PIV rating:      PIV ≥ V_m

**How to solve:**

1. If the DC level is given, work **backwards**: V<sub>m</sub> = V<sub>dc</sub> / 0.318 (then add V<sub>K</sub> if silicon).
2. Positive half-cycle: diode ON → output follows the input (minus V<sub>K</sub>), v<sub>d</sub> = V<sub>K</sub>.
3. Negative half-cycle: diode OFF → output = 0, and the **whole input appears across the diode**: v<sub>d</sub> = v<sub>i</sub>.
4. i<sub>d</sub> has the same shape as the output voltage, scaled by 1/R.

**Quick exam trick:**
> **0.318 for half-wave, 0.636 for full-wave.** When the diode is OFF, all the input voltage sits across the **diode**, so v<sub>d</sub> reaches −V<sub>m</sub>. That is the part students draw wrong.

---

### Type 5: Full-Wave Bridge Rectifier

**How to recognize this type:**

- Four diodes drawn in a **diamond**.
- Asks for v<sub>o</sub>, PIV, and maximum diode current.

**What I need to find:**

- Output peak, V<sub>dc</sub>, PIV of each diode, peak diode current.

**Given information:**

- Input peak, load resistance, diode type.

**Formula:**

    V_o(peak) = V_m − 2 V_K        (2 diodes conduct at once; ideal → V_m)
    V_dc = 0.636 × V_o(peak)
    PIV (bridge) = V_m
    I_max = V_o(peak) / R_L

**How to solve:**

1. Two diodes conduct on each half-cycle, so subtract **two** diode drops (zero if ideal).
2. V<sub>dc</sub> = 0.636 × peak output.
3. Each diode blocks V<sub>m</sub> when off → PIV = V<sub>m</sub>.
4. Peak diode current = peak load current.

**Quick exam trick:**
> **Bridge = two drops, PIV = V<sub>m</sub>, factor 0.636.** (For a centre-tapped transformer instead, PIV = 2V<sub>m</sub> — different circuit, do not mix them up.)

---

### Type 6: Clippers (the output is CUT OFF at a level)

**How to recognize this type:**

- Diode is in **parallel** with the output (shunt), or in series with a battery.
- The question says "determine v<sub>o</sub>" and shows a square or sine input.
- The output waveform keeps its shape but has a flat top or flat bottom.

**What I need to find:**

- The clipping level, and the value of v<sub>o</sub> in both states.

**Given information:**

- Input peak values, R, diode type, DC battery value **and its polarity**.

**Formula:**

    Clipping level  =  V_battery + V_K      (walk from the output node to ground
                                             through the branch, adding as you go)

    Diode ON  → v_o is held at the clipping level
    Diode OFF → no current in that branch → v_o follows the input
                (series clipper: v_o = 0 ; shunt clipper: v_o = v_i)

**How to solve:**

1. Find the **clipping level**: start at the output node, walk down the diode branch to ground, adding V<sub>K</sub> and the battery voltage with correct signs.
2. Decide when the diode turns on — compare v<sub>i</sub> against that level.
3. Write v<sub>o</sub> for both states.
4. Sketch: flat line at the clipping level for one state, the input shape for the other.

**Quick exam trick:**
> **Clipper = output is CUT.** Diode in parallel with the output → shunt clipper. Diode in series with the signal → series clipper. Battery pushes the clipping level up or down by its own voltage.

---

### Type 7: Clampers (the output is SHIFTED up or down)

**How to recognize this type:**

- There is a **capacitor in series** with the input. **This is the giveaway.**
- Diode and R are in parallel at the output.
- The output waveform has the **same peak-to-peak swing** as the input, just moved.

**What I need to find:**

- The capacitor voltage V<sub>C</sub>, then both output levels.

**Given information:**

- Input square/sine peaks, C, R, diode type, DC battery.

**Formula:**

    Step 1 — the half-cycle where the DIODE CONDUCTS:
        v_o = clamping level      (= V_battery ± V_K, same walk as a clipper)
        V_C = v_i − v_o           ← capacitor charges to this and HOLDS it
    Step 2 — the other half-cycle (diode OFF):
        v_o = v_i − V_C
    Check:  peak-to-peak of v_o must EQUAL peak-to-peak of v_i

**How to solve:**

1. Identify which half-cycle turns the diode ON.
2. In that half, v<sub>o</sub> = the clamping level. Compute V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub>.
3. In the other half, the diode is off: v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub> (V<sub>C</sub> is unchanged).
4. **Always check the swing matches the input swing.** If not, you made a sign error.

**Quick exam trick:**
> **Capacitor in series → clamper → same swing, shifted.** The peak-to-peak check catches almost every mistake.

---

### Type 8: Clamper Design

**How to recognize this type:**

- "Design a clamper to perform the function indicated in Fig. …".
- Shows an input waveform and the **desired** output waveform side by side.

**What I need to find:**

- The DC source value, the diode direction, and the R–C condition.

**Given information:**

- Both waveforms, and whether the diodes are ideal or silicon.

**Formula:**

    Shift = v_o(level) − v_i(level)           (must be the same for both levels)
    Clamping level = the output level that is HELD FLAT
    Required DC source:  V_battery = clamping level ∓ V_K
    Design rule:  5τ = 5RC  ≫  T/2

**How to solve:**

1. Compare the two waveforms — confirm the peak-to-peak values match.
2. Decide **which output level is the clamped one** (it is the one the diode holds).
3. Work out the DC source needed to sit at that level, remembering the V<sub>K</sub> offset.
4. Point the diode so it conducts during that half-cycle.
5. State 5RC ≫ T/2.

**Quick exam trick:**
> **Clamped level → tells you the battery. Direction of the shift → tells you which way the diode points.** Shifting up = clamp the bottom; shifting down = clamp the top.

---

### Type 9: R–C Time Constant Check

**How to recognize this type:**

- "Calculate 5τ" and "compare 5τ to half the period".

**What I need to find:**

- 5τ, T/2, and a comment.

**Given information:**

- R, C, and the frequency.

**Formula:**

    τ = R C          5τ = 5 R C
    T = 1 / f        half period = T / 2
    Good clamping if  5τ ≫ T/2

**How to solve:**

1. Multiply R × C (watch units: kΩ × µF = ms).
2. T = 1/f, halve it.
3. Compare and say by what factor.

**Quick exam trick:**
> **kΩ × µF = milliseconds.** 56 kΩ × 0.1 µF = 5.6 ms. That shortcut saves time and prevents power-of-ten errors.

---

### Type 10: Zener Regulator — Fixed V<sub>i</sub>, Variable R<sub>L</sub>

**How to recognize this type:**

- A Zener diode drawn in **parallel with the load**, R<sub>S</sub> in series with the supply.
- Asks for V<sub>L</sub>, I<sub>L</sub>, I<sub>Z</sub>, I<sub>R</sub> for given R<sub>L</sub> values.

**What I need to find:**

- First: **is the Zener ON or OFF?** Then the currents.

**Given information:**

- V<sub>i</sub>, R<sub>S</sub>, V<sub>Z</sub>, P<sub>Zmax</sub>, R<sub>L</sub>.

**Formula:**

    TEST FIRST — remove the Zener and compute:
        V = V_i × R_L / (R_S + R_L)
    If V < V_Z  → Zener OFF:  V_L = V,  I_Z = 0,  I_L = I_R = V / R_L
    If V ≥ V_Z  → Zener ON:
        V_L = V_Z
        I_R = (V_i − V_Z) / R_S
        I_L = V_Z / R_L
        I_Z = I_R − I_L
    Max power:   I_Zmax = P_Zmax / V_Z
    Min load:    R_Lmin = R_S V_Z / (V_i − V_Z)

**How to solve:**

1. **Always do the removal test first.** Never assume the Zener is on.
2. If off, it is just a voltage divider.
3. If on, V<sub>L</sub> is pinned at V<sub>Z</sub>; find I<sub>R</sub> and I<sub>L</sub>, subtract for I<sub>Z</sub>.
4. For "maximum power", set I<sub>Z</sub> = P<sub>Zmax</sub>/V<sub>Z</sub> and work back to R<sub>L</sub>.

**Quick exam trick:**
> **Test before you trust.** Compute the open-circuit divider voltage first. Also remember I<sub>R</sub> is **constant** whenever the Zener is on — only I<sub>L</sub> and I<sub>Z</sub> trade places.

---

### Type 11: Zener Regulator — Find the Range of V<sub>i</sub>

**How to recognize this type:**

- R<sub>L</sub> is **fixed**, and the question asks for the "range of V<sub>i</sub>".

**What I need to find:**

- V<sub>imin</sub> and V<sub>imax</sub>.

**Given information:**

- R<sub>S</sub>, V<sub>Z</sub>, P<sub>Zmax</sub>, fixed R<sub>L</sub>.

**Formula:**

    I_L = V_Z / R_L                       (fixed, because R_L is fixed)
    I_Zmax = P_Zmax / V_Z
    V_i(min) = V_Z + I_L R_S                       ← Zener just barely on, I_Z = 0
    V_i(max) = V_Z + (I_L + I_Zmax) R_S            ← Zener at full power

**How to solve:**

1. I<sub>L</sub> is fixed — compute it once.
2. Minimum: the Zener is about to turn on, so I<sub>Z</sub> = 0 and I<sub>R</sub> = I<sub>L</sub>.
3. Maximum: I<sub>Z</sub> is at its rated limit, so I<sub>R</sub> = I<sub>L</sub> + I<sub>Zmax</sub>.
4. Both times: V<sub>i</sub> = V<sub>Z</sub> + I<sub>R</sub>R<sub>S</sub>.

**Quick exam trick:**
> **Two extremes: I<sub>Z</sub> = 0 and I<sub>Z</sub> = I<sub>Zmax</sub>.** Same formula, two numbers.

---

### Type 12: Zener Design

**How to recognize this type:**

- "Design the network … to maintain V<sub>L</sub> at … for a load variation from 0 mA to …".

**What I need to find:**

- V<sub>Z</sub>, R<sub>S</sub>, and P<sub>Zmax</sub>.

**Given information:**

- V<sub>i</sub>, the required V<sub>L</sub>, and the load current range.

**Formula:**

    V_Z = V_L                                  (the Zener sets the output)
    R_S = (V_i − V_Z) / I_L(max)               (size R_S for the heaviest load)
    Worst case for the Zener is I_L = 0:
    P_Zmax = V_Z × I_L(max)

**How to solve:**

1. V<sub>Z</sub> is simply the required output voltage.
2. Size R<sub>S</sub> at the **maximum** load current (that is when the Zener has least to spare).
3. The Zener's worst case is the **minimum** load (I<sub>L</sub> = 0), when it must absorb all of I<sub>R</sub>.
4. P = V<sub>Z</sub> × that current.

**Quick exam trick:**
> **R<sub>S</sub> is sized at max load; the Zener's power is rated at min load.** Opposite extremes — that is the whole trick.

<div class="pagebreak"></div>

# PART 2 — COMPLETE FORMULA SHEET

Only the formulas needed for the questions in your document.

## Chapter 4 — BJT DC Biasing

### Universal BJT relations (true in every configuration)

| Formula | Symbols | Unit | When to use |
|---|---|---|---|
| I<sub>E</sub> = I<sub>C</sub> + I<sub>B</sub> | terminal currents | A | Always true |
| I<sub>C</sub> = β I<sub>B</sub> | β = current gain | A | Active region |
| I<sub>E</sub> = (β + 1) I<sub>B</sub> | — | A | Active region |
| α = β / (β + 1) | α ≈ 0.99 | — | Common base, current sources |
| I<sub>C</sub> = α I<sub>E</sub> | — | A | When I<sub>E</sub> is known first |
| V<sub>BE</sub> = 0.7 V | base–emitter drop | V | Silicon, always |
| V<sub>B</sub> = V<sub>E</sub> + 0.7 | node voltages | V | Links base and emitter sides |
| V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> | — | V | Always |

### Fixed bias

| Formula | Unit | When to use |
|---|---|---|
| I<sub>B</sub> = (V<sub>CC</sub> − 0.7) / R<sub>B</sub> | A | Emitter grounded, single R<sub>B</sub> |
| V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub> | V | Collector loop |
| I<sub>Csat</sub> = V<sub>CC</sub> / R<sub>C</sub> | A | Saturation, no R<sub>E</sub> |

### Emitter bias

| Formula | Unit | When to use |
|---|---|---|
| I<sub>B</sub> = (V<sub>CC</sub> − 0.7) / [R<sub>B</sub> + (β+1)R<sub>E</sub>] | A | R<sub>B</sub> to V<sub>CC</sub> plus R<sub>E</sub> |
| V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> | V | Emitter node |
| V<sub>C</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub> | V | Collector node |
| I<sub>Csat</sub> = V<sub>CC</sub> / (R<sub>C</sub> + R<sub>E</sub>) | A | Saturation with R<sub>E</sub> |

### Voltage-divider bias

| Formula | Unit | When to use |
|---|---|---|
| R<sub>Th</sub> = R<sub>1</sub>R<sub>2</sub> / (R<sub>1</sub> + R<sub>2</sub>) | Ω | Exact method |
| E<sub>Th</sub> = V<sub>CC</sub>R<sub>2</sub> / (R<sub>1</sub> + R<sub>2</sub>) | V | Exact method |
| I<sub>B</sub> = (E<sub>Th</sub> − 0.7) / [R<sub>Th</sub> + (β+1)R<sub>E</sub>] | A | Exact method |
| βR<sub>E</sub> ≥ 10R<sub>2</sub> | — | **Eq. 4.33** — test before approximating |
| V<sub>B</sub> = V<sub>CC</sub>R<sub>2</sub> / (R<sub>1</sub> + R<sub>2</sub>) | V | Approximate method |
| V<sub>E</sub> = V<sub>B</sub> − 0.7, I<sub>E</sub> = V<sub>E</sub>/R<sub>E</sub> | V, A | Approximate method |
| V<sub>CE</sub> = V<sub>CC</sub> − I<sub>C</sub>(R<sub>C</sub> + R<sub>E</sub>) | V | Approximate method |
| I<sub>2</sub> = V<sub>B</sub>/R<sub>2</sub>, I<sub>1</sub> = I<sub>2</sub> + I<sub>B</sub> | A | Reverse problems — finding R<sub>1</sub> |

### Collector-feedback bias

| Formula | Unit | When to use |
|---|---|---|
| I<sub>B</sub> = (V<sub>CC</sub> − 0.7) / [R<sub>F</sub> + β(R<sub>C</sub> + R<sub>E</sub>)] | A | R<sub>F</sub> from base to collector |
| V<sub>C</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub> | V | Collector node |
| I<sub>B</sub> = (V<sub>C</sub> − V<sub>B</sub>) / R<sub>F</sub> | A | Reverse problems |

### Common base

| Formula | Unit | When to use |
|---|---|---|
| V<sub>E</sub> = V<sub>B</sub> − 0.7 | V | Base grounded or at a fixed voltage |
| I<sub>E</sub> = (V<sub>E</sub> − V<sub>EE</sub>) / R<sub>E</sub> | A | Emitter loop |
| V<sub>BC</sub> = V<sub>B</sub> − V<sub>C</sub> | V | When asked |

### Design

| Formula | Unit | When to use |
|---|---|---|
| R<sub>C</sub> = (V<sub>CC</sub> − V<sub>CEQ</sub> − V<sub>E</sub>) / I<sub>CQ</sub> | Ω | Sizing R<sub>C</sub> |
| R<sub>E</sub> = V<sub>E</sub> / I<sub>E</sub> | Ω | Sizing R<sub>E</sub> |
| R<sub>B</sub> = (V<sub>CC</sub> − 0.7 − V<sub>E</sub>) / I<sub>B</sub> | Ω | Sizing R<sub>B</sub> |
| R<sub>2</sub> ≤ βR<sub>E</sub>/10 | Ω | Choosing R<sub>2</sub> in a divider design |
| R<sub>1</sub> = V<sub>CC</sub>R<sub>2</sub>/V<sub>B</sub> − R<sub>2</sub> | Ω | Choosing R<sub>1</sub> |

**Standard resistor values (E24, ×10<sup>n</sup>):**
1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1

## Chapter 1 — Diode Equation

| Formula | Symbols | Unit | When to use |
|---|---|---|---|
| T<sub>K</sub> = T<sub>C</sub> + 273 | temperature | K | Always first |
| V<sub>T</sub> = kT<sub>K</sub>/q = (8.62×10<sup>−5</sup>)T<sub>K</sub> | thermal voltage | V | Every diode-equation problem |
| I<sub>D</sub> = I<sub>s</sub>(e<sup>V<sub>D</sub>/(nV<sub>T</sub>)</sup> − 1) | **Eq. 1.2**, Shockley | A | Find current from voltage |
| I<sub>s</sub> = I<sub>D</sub> / (e<sup>V<sub>D</sub>/(nV<sub>T</sub>)</sup> − 1) | saturation current | A | Find I<sub>s</sub> |
| V<sub>D</sub> = nV<sub>T</sub> ln(I<sub>D</sub>/I<sub>s</sub> + 1) | — | V | Find voltage from current |
| I<sub>D</sub> ≈ −I<sub>s</sub> | — | A | Reverse bias (large negative V<sub>D</sub>) |

- n = ideality factor: **1** at high current, **2** at low current. It multiplies V<sub>T</sub>.
- At 25 °C, V<sub>T</sub> ≈ 25.7 mV (commonly rounded to 26 mV).

## Chapter 2 — Diode Applications

### Diode drops

| Material | V<sub>K</sub> |
|---|---|
| Ideal | 0 V |
| Germanium (Ge) | 0.3 V |
| Silicon (Si) | 0.7 V |
| Gallium Arsenide (GaAs) | 1.2 V |

### DC diode circuits

| Formula | Unit | When to use |
|---|---|---|
| I = (ΣV − ΣV<sub>K</sub>) / ΣR | A | Series loop, all diodes ON |
| I = 0, V<sub>o</sub> = 0 | — | Any diode reverse-biased |
| Opposing diodes → open circuit | — | Back-to-back pair |
| KCL at the output node | — | Parallel diode branches |

### Rectifiers

| Formula | Unit | When to use |
|---|---|---|
| V<sub>dc</sub> = 0.318V<sub>m</sub> | V | Half-wave, ideal |
| V<sub>dc</sub> = 0.318(V<sub>m</sub> − 0.7) | V | Half-wave, silicon |
| V<sub>dc</sub> = 0.636V<sub>m</sub> | V | Full-wave (bridge) |
| V<sub>o(peak)</sub> = V<sub>m</sub> − 2V<sub>K</sub> | V | Bridge (two diodes conduct) |
| PIV = V<sub>m</sub> | V | Half-wave and bridge |
| I<sub>max</sub> = V<sub>o(peak)</sub>/R<sub>L</sub> | A | Peak diode current |
| T = 1/f | s | Period |

### Clippers and clampers

| Formula | Unit | When to use |
|---|---|---|
| Clipping level = V<sub>battery</sub> + V<sub>K</sub> | V | Clipper — walk the diode branch |
| V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub> (during conduction) | V | Clamper step 1 |
| v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub> (diode off) | V | Clamper step 2 |
| v<sub>o</sub>(p-p) = v<sub>i</sub>(p-p) | V | **Clamper check** |
| 5τ = 5RC ≫ T/2 | s | Clamper design rule |

### Zener regulators

| Formula | Unit | When to use |
|---|---|---|
| V = V<sub>i</sub>R<sub>L</sub>/(R<sub>S</sub> + R<sub>L</sub>) | V | **Test** — Zener removed |
| V<sub>L</sub> = V<sub>Z</sub> | V | Zener ON |
| I<sub>R</sub> = (V<sub>i</sub> − V<sub>Z</sub>)/R<sub>S</sub> | A | Zener ON |
| I<sub>L</sub> = V<sub>Z</sub>/R<sub>L</sub> | A | Zener ON |
| I<sub>Z</sub> = I<sub>R</sub> − I<sub>L</sub> | A | Zener ON |
| I<sub>Zmax</sub> = P<sub>Zmax</sub>/V<sub>Z</sub> | A | Power limit |
| R<sub>Lmin</sub> = R<sub>S</sub>V<sub>Z</sub>/(V<sub>i</sub> − V<sub>Z</sub>) | Ω | Smallest load that keeps Zener on |
| V<sub>i(min)</sub> = V<sub>Z</sub> + I<sub>L</sub>R<sub>S</sub> | V | Range of V<sub>i</sub> |
| V<sub>i(max)</sub> = V<sub>Z</sub> + (I<sub>L</sub> + I<sub>Zmax</sub>)R<sub>S</sub> | V | Range of V<sub>i</sub> |
| P<sub>Z</sub> = V<sub>Z</sub>I<sub>Z</sub> | W | Power check |

<div class="pagebreak"></div>

# PART 3 — ALL QUESTIONS SOLVED

Questions appear in the same order as your document: **Chapter 4 → Chapter 1 → Chapter 2**.

# Chapter 4 — BJT DC Biasing

## Fixed-Bias Configuration

### Question 1 — Fig. 4.118

**Problem Type:** Fixed Bias → Find the Q-point (Type 1)

**Circuit values read from Fig. 4.118:** V<sub>CC</sub> = 16 V, R<sub>B</sub> = 510 kΩ, R<sub>C</sub> = 1.8 kΩ, β = 120

**Given:**

- V<sub>CC</sub> = 16 V, R<sub>B</sub> = 510 kΩ, R<sub>C</sub> = 1.8 kΩ, β = 120
- Emitter connected directly to ground

**Find:**

- I<sub>BQ</sub>, I<sub>CQ</sub>, V<sub>CEQ</sub>, V<sub>C</sub>, V<sub>B</sub>, V<sub>E</sub>

**Formula:**

    I_B = (V_CC − 0.7)/R_B ;  I_C = β I_B ;  V_CE = V_CC − I_C R_C

**Solution:**

1. I<sub>BQ</sub> = (16 − 0.7) / 510 kΩ = 15.3 / 510 000 = **30 µA**
2. I<sub>CQ</sub> = 120 × 30 µA = **3.6 mA**
3. V<sub>CEQ</sub> = 16 − (3.6 mA)(1.8 kΩ) = 16 − 6.48 = **9.52 V**
4. Emitter grounded → V<sub>E</sub> = 0 V
5. V<sub>C</sub> = V<sub>CEQ</sub> + V<sub>E</sub> = **9.52 V**
6. V<sub>B</sub> = V<sub>E</sub> + 0.7 = **0.7 V**

**Answer:**

- **(a)** I<sub>BQ</sub> = 30 µA  (b) I<sub>CQ</sub> = 3.6 mA  (c) V<sub>CEQ</sub> = 9.52 V
- **(d)** V<sub>C</sub> = 9.52 V  (e) V<sub>B</sub> = 0.7 V  (f) V<sub>E</sub> = 0 V

---

### Question 2 — Fig. 4.119

**Problem Type:** Fixed Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.119:** V<sub>CC</sub> = 12 V, I<sub>B</sub> = 40 µA, β = 80, V<sub>C</sub> = 6 V; R<sub>B</sub> and R<sub>C</sub> unknown

**Given:**

- V<sub>CC</sub> = 12 V, I<sub>B</sub> = 40 µA, β = 80, V<sub>C</sub> = 6 V, emitter grounded

**Find:**

- I<sub>C</sub>, R<sub>C</sub>, R<sub>B</sub>, V<sub>CE</sub>

**Formula:**

    I_C = β I_B ;  R_C = (V_CC − V_C)/I_C ;  R_B = (V_CC − 0.7)/I_B ;  V_CE = V_C − V_E

**Solution:**

1. I<sub>C</sub> = 80 × 40 µA = **3.2 mA**
2. Voltage across R<sub>C</sub> = 12 − 6 = 6 V
   R<sub>C</sub> = 6 / 3.2 mA = **1.875 kΩ**

3. R<sub>B</sub> = (12 − 0.7) / 40 µA = 11.3 / 40×10<sup>−6</sup> = **282.5 kΩ**
4. Emitter grounded → V<sub>E</sub> = 0, so V<sub>CE</sub> = V<sub>C</sub> = **6 V**

**Answer:**

- **(a)** I<sub>C</sub> = 3.2 mA  (b) R<sub>C</sub> = 1.875 kΩ  (c) R<sub>B</sub> = 282.5 kΩ  (d) V<sub>CE</sub> = 6 V

---

### Question 3 — Fig. 4.120

**Problem Type:** Fixed Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.120:** R<sub>C</sub> = 2.2 kΩ, I<sub>B</sub> = 20 µA, I<sub>E</sub> = 4 mA, V<sub>CE</sub> = 7.2 V; V<sub>CC</sub>, β, R<sub>B</sub> unknown

**Given:**

- R<sub>C</sub> = 2.2 kΩ, I<sub>B</sub> = 20 µA, I<sub>E</sub> = 4 mA, V<sub>CE</sub> = 7.2 V, emitter grounded

**Find:**

- I<sub>C</sub>, V<sub>CC</sub>, β, R<sub>B</sub>

**Formula:**

    I_C = I_E − I_B ;  V_CC = V_CE + I_C R_C ;  β = I_C/I_B ;  R_B = (V_CC − 0.7)/I_B

**Solution:**

1. I<sub>C</sub> = I<sub>E</sub> − I<sub>B</sub> = 4 mA − 0.02 mA = **3.98 mA**
2. Drop across R<sub>C</sub> = (3.98 mA)(2.2 kΩ) = 8.756 V
   V<sub>CC</sub> = 7.2 + 8.756 = **15.96 V**

3. β = I<sub>C</sub>/I<sub>B</sub> = 3.98 mA / 20 µA = **199**
4. R<sub>B</sub> = (15.96 − 0.7) / 20 µA = 15.26 / 20×10<sup>−6</sup> = **762.8 kΩ**

**Answer:**

- **(a)** I<sub>C</sub> = 3.98 mA  (b) V<sub>CC</sub> = 15.96 V  (c) β = 199  (d) R<sub>B</sub> = 762.8 kΩ

---

### Question 4 — Fig. 4.118

**Problem Type:** Saturation current, fixed bias (Type 7)

**Given:**

- V<sub>CC</sub> = 16 V, R<sub>C</sub> = 1.8 kΩ (no R<sub>E</sub>)

**Find:**

- I<sub>Csat</sub>

**Formula:**

    I_Csat = V_CC / R_C

**Solution:**

1. Short the transistor (V<sub>CE</sub> = 0). Only R<sub>C</sub> limits the current.
2. I<sub>Csat</sub> = 16 / 1800 = **8.89 mA**

**Answer:**

- I<sub>Csat</sub> = 8.89 mA
- *Note:* I<sub>CQ</sub> from Q1 was 3.6 mA, which is well under 8.89 mA — the transistor is properly in the active region.

## Emitter-Bias Configuration

### Question 8 — Fig. 4.122

**Problem Type:** Emitter Bias → Find the Q-point (Type 2)

**Circuit values read from Fig. 4.122:** V<sub>CC</sub> = 20 V, R<sub>B</sub> = 270 kΩ, R<sub>C</sub> = 470 Ω, R<sub>E</sub> = 2.2 kΩ, β = 125

**Given:**

- V<sub>CC</sub> = 20 V, R<sub>B</sub> = 270 kΩ, R<sub>C</sub> = 470 Ω, R<sub>E</sub> = 2.2 kΩ, β = 125

**Find:**

- I<sub>BQ</sub>, I<sub>CQ</sub>, V<sub>CEQ</sub>, V<sub>C</sub>, V<sub>B</sub>, V<sub>E</sub>

**Formula:**

    I_B = (V_CC − 0.7)/[R_B + (β+1)R_E]

**Solution:**

1. Denominator: (β+1)R<sub>E</sub> = 126 × 2200 = 277 200 Ω
   R<sub>B</sub> + (β+1)R<sub>E</sub> = 270 000 + 277 200 = 547 200 Ω

2. I<sub>BQ</sub> = (20 − 0.7) / 547 200 = 19.3 / 547 200 = **35.27 µA**
3. I<sub>CQ</sub> = 125 × 35.27 µA = **4.41 mA**
4. I<sub>E</sub> = 126 × 35.27 µA = 4.44 mA
5. V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> = (4.44 mA)(2.2 kΩ) = **9.78 V**
6. V<sub>C</sub> = 20 − (4.41 mA)(470 Ω) = 20 − 2.07 = **17.93 V**
7. V<sub>CEQ</sub> = V<sub>C</sub> − V<sub>E</sub> = 17.93 − 9.78 = **8.15 V**
8. V<sub>B</sub> = V<sub>E</sub> + 0.7 = **10.48 V**

**Answer:**

- **(a)** I<sub>BQ</sub> = 35.27 µA  (b) I<sub>CQ</sub> = 4.41 mA  (c) V<sub>CEQ</sub> = 8.15 V
- **(d)** V<sub>C</sub> = 17.93 V  (e) V<sub>B</sub> = 10.48 V  (f) V<sub>E</sub> = 9.78 V

---

### Question 12 — Fig. 4.122

**Problem Type:** Saturation current with R<sub>E</sub> (Type 7)

**Given:**

- V<sub>CC</sub> = 20 V, R<sub>C</sub> = 470 Ω, R<sub>E</sub> = 2.2 kΩ

**Find:**

- I<sub>Csat</sub>

**Formula:**

    I_Csat = V_CC / (R_C + R_E)

**Solution:**

1. R<sub>C</sub> + R<sub>E</sub> = 470 + 2200 = 2670 Ω
2. I<sub>Csat</sub> = 20 / 2670 = **7.49 mA**

**Answer:**

- I<sub>Csat</sub> = 7.49 mA (compare with I<sub>CQ</sub> = 4.41 mA from Q8 — active region confirmed)

---

### Question 10 — Fig. 4.123

**Problem Type:** Emitter Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.123:** V<sub>CC</sub> = 12 V, I<sub>C</sub> = 2 mA, V<sub>C</sub> = 7.6 V, V<sub>E</sub> = 2.4 V, β = 80; R<sub>B</sub>, R<sub>C</sub>, R<sub>E</sub> unknown

**Given:**

- V<sub>CC</sub> = 12 V, I<sub>C</sub> = 2 mA, V<sub>C</sub> = 7.6 V, V<sub>E</sub> = 2.4 V, β = 80

**Find:**

- R<sub>C</sub>, R<sub>E</sub>, R<sub>B</sub>, V<sub>CE</sub>, V<sub>B</sub>

**Formula:**

    R_C = (V_CC − V_C)/I_C ;  I_E = I_C(β+1)/β ;  R_E = V_E/I_E
    V_B = V_E + 0.7 ;  I_B = I_C/β ;  R_B = (V_CC − V_B)/I_B

**Solution:**

1. Drop across R<sub>C</sub> = 12 − 7.6 = 4.4 V
   R<sub>C</sub> = 4.4 / 2 mA = **2.2 kΩ**

2. I<sub>E</sub> = I<sub>C</sub>(β+1)/β = 2 mA × 81/80 = 2.025 mA
   R<sub>E</sub> = 2.4 / 2.025 mA = **1.185 kΩ**

3. V<sub>B</sub> = 2.4 + 0.7 = **3.1 V**
4. I<sub>B</sub> = 2 mA / 80 = 25 µA
   R<sub>B</sub> = (12 − 3.1) / 25 µA = 8.9 / 25×10<sup>−6</sup> = **356 kΩ**

5. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 7.6 − 2.4 = **5.2 V**

**Answer:**

- **(a)** R<sub>C</sub> = 2.2 kΩ  (b) R<sub>E</sub> = 1.185 kΩ  (c) R<sub>B</sub> = 356 kΩ
- **(d)** V<sub>CE</sub> = 5.2 V  (e) V<sub>B</sub> = 3.1 V

---

### Question 11 — Fig. 4.124

**Problem Type:** Emitter Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.124:** I<sub>B</sub> = 20 µA, R<sub>C</sub> = 2.7 kΩ, V<sub>CE</sub> = 7.3 V, V<sub>E</sub> = 2.1 V, R<sub>E</sub> = 0.68 kΩ; β, V<sub>CC</sub>, R<sub>B</sub> unknown

**Given:**

- I<sub>B</sub> = 20 µA, R<sub>C</sub> = 2.7 kΩ, V<sub>CE</sub> = 7.3 V, V<sub>E</sub> = 2.1 V, R<sub>E</sub> = 0.68 kΩ

**Find:**

- β, V<sub>CC</sub>, R<sub>B</sub>

**Formula:**

    I_E = V_E/R_E ;  I_C = I_E − I_B ;  β = I_C/I_B
    V_CC = V_CE + I_C R_C + V_E ;  R_B = (V_CC − V_B)/I_B

**Solution:**

1. I<sub>E</sub> = 2.1 / 680 = 3.088 mA
2. I<sub>C</sub> = 3.088 − 0.02 = 3.068 mA
3. β = 3.068 mA / 20 µA = **153.4**
4. Drop across R<sub>C</sub> = (3.068 mA)(2.7 kΩ) = 8.28 V
   V<sub>CC</sub> = 7.3 + 8.28 + 2.1 = **17.68 V**

5. V<sub>B</sub> = V<sub>E</sub> + 0.7 = 2.8 V
   R<sub>B</sub> = (17.68 − 2.8) / 20 µA = 14.88 / 20×10<sup>−6</sup> = **744 kΩ**

**Answer:**

- **(a)** β = 153.4  (b) V<sub>CC</sub> = 17.68 V  (c) R<sub>B</sub> = 744 kΩ

## Voltage-Divider Bias Configuration

### Question 15 — Fig. 4.125

**Problem Type:** Voltage-Divider Bias → Exact (Thévenin) method (Type 3)

**Circuit values read from Fig. 4.125:** V<sub>CC</sub> = 16 V, R<sub>1</sub> = 62 kΩ, R<sub>2</sub> = 9.1 kΩ, R<sub>C</sub> = 3.9 kΩ, R<sub>E</sub> = 0.68 kΩ, β = 80

**Given:**

- V<sub>CC</sub> = 16 V, R<sub>1</sub> = 62 kΩ, R<sub>2</sub> = 9.1 kΩ, R<sub>C</sub> = 3.9 kΩ, R<sub>E</sub> = 0.68 kΩ, β = 80

**Find:**

- I<sub>BQ</sub>, I<sub>CQ</sub>, V<sub>CEQ</sub>, V<sub>C</sub>, V<sub>E</sub>, V<sub>B</sub>

**Formula:**

    R_Th = R_1R_2/(R_1+R_2) ;  E_Th = V_CC R_2/(R_1+R_2)
    I_B = (E_Th − 0.7)/[R_Th + (β+1)R_E]

**Solution:**

1. R<sub>Th</sub> = (62 × 9.1)/(62 + 9.1) kΩ = 564.2/71.1 = **7.94 kΩ**
2. E<sub>Th</sub> = 16 × 9.1/71.1 = 145.6/71.1 = **2.048 V**
3. Denominator = 7940 + 81(680) = 7940 + 55 080 = 63 020 Ω
4. I<sub>BQ</sub> = (2.048 − 0.7) / 63 020 = 1.348 / 63 020 = **21.39 µA**
5. I<sub>CQ</sub> = 80 × 21.39 µA = **1.71 mA**
6. I<sub>E</sub> = 81 × 21.39 µA = 1.733 mA
   V<sub>E</sub> = (1.733 mA)(680 Ω) = **1.18 V**

7. V<sub>C</sub> = 16 − (1.71 mA)(3.9 kΩ) = 16 − 6.67 = **9.33 V**
8. V<sub>CEQ</sub> = 9.33 − 1.18 = **8.15 V**
9. V<sub>B</sub> = 1.18 + 0.7 = **1.88 V**

**Answer:**

- **(a)** I<sub>BQ</sub> = 21.39 µA  (b) I<sub>CQ</sub> = 1.71 mA  (c) V<sub>CEQ</sub> = 8.15 V
- **(d)** V<sub>C</sub> = 9.33 V  (e) V<sub>E</sub> = 1.18 V  (f) V<sub>B</sub> = 1.88 V

---

### Question 17 — Fig. 4.126

**Problem Type:** Voltage-Divider Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.126:** V<sub>CC</sub> = 18 V, R<sub>C</sub> = 4.7 kΩ, V<sub>C</sub> = 12 V, R<sub>2</sub> = 5.6 kΩ, R<sub>E</sub> = 1.2 kΩ; R<sub>1</sub> unknown

**Given:**

- V<sub>CC</sub> = 18 V, R<sub>C</sub> = 4.7 kΩ, V<sub>C</sub> = 12 V, R<sub>2</sub> = 5.6 kΩ, R<sub>E</sub> = 1.2 kΩ
- β is not given, so use I<sub>E</sub> ≈ I<sub>C</sub>

**Find:**

- I<sub>C</sub>, V<sub>E</sub>, V<sub>B</sub>, R<sub>1</sub>

**Formula:**

    I_C = (V_CC − V_C)/R_C ;  V_E ≈ I_C R_E ;  V_B = V_E + 0.7
    V_B = V_CC R_2/(R_1+R_2)  →  R_1 = V_CC R_2/V_B − R_2

**Solution:**

1. Drop across R<sub>C</sub> = 18 − 12 = 6 V
   I<sub>C</sub> = 6 / 4.7 kΩ = **1.277 mA**

2. V<sub>E</sub> = (1.277 mA)(1.2 kΩ) = **1.53 V**
3. V<sub>B</sub> = 1.53 + 0.7 = **2.23 V**
4. From the divider: R<sub>1</sub> + R<sub>2</sub> = V<sub>CC</sub>R<sub>2</sub>/V<sub>B</sub> = (18 × 5.6 kΩ)/2.23 = 100.8/2.23 = 45.16 kΩ
   R<sub>1</sub> = 45.16 − 5.6 = **39.56 kΩ**

**Answer:**

- **(a)** I<sub>C</sub> = 1.277 mA  (b) V<sub>E</sub> = 1.53 V  (c) V<sub>B</sub> = 2.23 V  (d) R<sub>1</sub> = 39.56 kΩ

---

### Question 19 — Fig. 4.125

**Problem Type:** Saturation current with R<sub>E</sub> (Type 7)

**Given:**

- V<sub>CC</sub> = 16 V, R<sub>C</sub> = 3.9 kΩ, R<sub>E</sub> = 0.68 kΩ

**Find:**

- I<sub>Csat</sub>

**Formula:**

    I_Csat = V_CC/(R_C + R_E)

**Solution:**

1. R<sub>C</sub> + R<sub>E</sub> = 3900 + 680 = 4580 Ω
2. I<sub>Csat</sub> = 16 / 4580 = **3.49 mA**

**Answer:**

- I<sub>Csat</sub> = 3.49 mA (I<sub>CQ</sub> was 1.71 mA — active region)

---

### Question 18 — Fig. 4.127

**Problem Type:** Voltage-Divider Bias → Reverse problem (Type 8)

**Circuit values read from Fig. 4.127:** R<sub>C</sub> = 2.7 kΩ, V<sub>C</sub> = 10.6 V, I<sub>B</sub> = 20 µA, β = 100, R<sub>2</sub> = 8.2 kΩ, R<sub>E</sub> = 1.2 kΩ; V<sub>CC</sub> and R<sub>1</sub> unknown

**Given:**

- R<sub>C</sub> = 2.7 kΩ, V<sub>C</sub> = 10.6 V, I<sub>B</sub> = 20 µA, β = 100, R<sub>2</sub> = 8.2 kΩ, R<sub>E</sub> = 1.2 kΩ

**Find:**

- I<sub>C</sub>, V<sub>E</sub>, V<sub>CC</sub>, V<sub>CE</sub>, V<sub>B</sub>, R<sub>1</sub>

**Formula:**

    I_C = β I_B ;  I_E = (β+1)I_B ;  V_E = I_E R_E ;  V_CC = V_C + I_C R_C
    I_2 = V_B/R_2 ;  I_1 = I_2 + I_B ;  R_1 = (V_CC − V_B)/I_1

**Solution:**

1. I<sub>C</sub> = 100 × 20 µA = **2 mA**
2. I<sub>E</sub> = 101 × 20 µA = 2.02 mA
   V<sub>E</sub> = (2.02 mA)(1.2 kΩ) = **2.42 V**

3. V<sub>CC</sub> = V<sub>C</sub> + I<sub>C</sub>R<sub>C</sub> = 10.6 + (2 mA)(2.7 kΩ) = 10.6 + 5.4 = **16 V**
4. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 10.6 − 2.42 = **8.18 V**
5. V<sub>B</sub> = V<sub>E</sub> + 0.7 = **3.12 V**
6. Current through R<sub>2</sub>: I<sub>2</sub> = 3.12 / 8.2 kΩ = 0.381 mA
   Current through R<sub>1</sub>: I<sub>1</sub> = I<sub>2</sub> + I<sub>B</sub> = 0.381 + 0.020 = 0.401 mA
   R<sub>1</sub> = (16 − 3.12) / 0.401 mA = 12.88 / 0.401 mA = **32.11 kΩ**

**Answer:**

- **(a)** I<sub>C</sub> = 2 mA  (b) V<sub>E</sub> = 2.42 V  (c) V<sub>CC</sub> = 16 V
- **(d)** V<sub>CE</sub> = 8.18 V  (e) V<sub>B</sub> = 3.12 V  (f) R<sub>1</sub> = 32.11 kΩ

> **Watch out:** in step 6, I<sub>1</sub> must include I<sub>B</sub>. Using I<sub>1</sub> = I<sub>2</sub> alone gives 33.8 kΩ, which is wrong.

---

### Question 21 — Fig. 4.128 (approximate approach)

**Problem Type:** Voltage-Divider Bias → Approximate method (Type 3)

**Circuit values read from Fig. 4.128:** V<sub>CC</sub> = 18 V, R<sub>1</sub> = 39 kΩ, R<sub>2</sub> = 8.2 kΩ, R<sub>C</sub> = 3.3 kΩ, R<sub>E</sub> = 1 kΩ, β = 120

**Given:**

- V<sub>CC</sub> = 18 V, R<sub>1</sub> = 39 kΩ, R<sub>2</sub> = 8.2 kΩ, R<sub>C</sub> = 3.3 kΩ, R<sub>E</sub> = 1 kΩ, β = 120

**Find:**

- First check Eq. (4.33), then I<sub>C</sub>, V<sub>CE</sub>, I<sub>B</sub>, V<sub>E</sub>, V<sub>B</sub>

**Formula:**

    Check:  β R_E ≥ 10 R_2
    V_B = V_CC R_2/(R_1+R_2) ;  V_E = V_B − 0.7 ;  I_E = V_E/R_E ≈ I_C
    V_CE = V_CC − I_C(R_C + R_E) ;  I_B = I_C/β

**Solution:**

1. **Check Eq. (4.33):** βR<sub>E</sub> = 120 × 1000 = 120 000 Ω; 10R<sub>2</sub> = 10 × 8200 = 82 000 Ω
   120 kΩ ≥ 82 kΩ → **condition satisfied**, approximate approach is allowed.

2. V<sub>B</sub> = 18 × 8.2/(39 + 8.2) = 147.6/47.2 = **3.13 V**
3. V<sub>E</sub> = 3.13 − 0.7 = **2.43 V**
4. I<sub>E</sub> = 2.43 / 1000 = 2.427 mA, and I<sub>C</sub> ≈ I<sub>E</sub> = **2.43 mA**
5. V<sub>CE</sub> = 18 − (2.427 mA)(3.3 kΩ + 1 kΩ) = 18 − (2.427 mA)(4.3 kΩ) = 18 − 10.44 = **7.56 V**
6. I<sub>B</sub> = 2.427 mA / 120 = **20.23 µA**

**Answer:**

- **(a)** I<sub>C</sub> = 2.43 mA  (b) V<sub>CE</sub> = 7.56 V  (c) I<sub>B</sub> = 20.23 µA
- **(d)** V<sub>E</sub> = 2.43 V  (e) V<sub>B</sub> = 3.13 V

---

### Question 22 — Fig. 4.128 (exact / Thévenin approach + comparison)

**Problem Type:** Voltage-Divider Bias → Exact method, then compare (Type 3)

**Given:**

- Same circuit as Question 21

**Find:**

- The same five quantities using Thévenin, then compare with Q21

**Formula:**

    R_Th = R_1R_2/(R_1+R_2) ;  E_Th = V_CC R_2/(R_1+R_2)
    I_B = (E_Th − 0.7)/[R_Th + (β+1)R_E]

**Solution:**

1. R<sub>Th</sub> = (39 × 8.2)/(39 + 8.2) = 319.8/47.2 = **6.78 kΩ**
2. E<sub>Th</sub> = 18 × 8.2/47.2 = **3.13 V** (same as V<sub>B</sub> in Q21)
3. Denominator = 6775 + 121(1000) = 6775 + 121 000 = 127 775 Ω
4. I<sub>B</sub> = (3.127 − 0.7) / 127 775 = 2.427 / 127 775 = **19.0 µA**
5. I<sub>C</sub> = 120 × 19.0 µA = **2.28 mA**
6. I<sub>E</sub> = 121 × 19.0 µA = 2.298 mA
   V<sub>E</sub> = (2.298 mA)(1 kΩ) = **2.30 V**

7. V<sub>CE</sub> = 18 − (2.28 mA)(3.3 kΩ) − (2.298 mA)(1 kΩ) = 18 − 7.52 − 2.30 = **8.18 V**
8. V<sub>B</sub> = 2.30 + 0.7 = **3.00 V**

**Comparison:**

| Quantity | Approximate (Q21) | Exact (Q22) | Difference |
|---|---|---|---|
| I<sub>B</sub> | 20.23 µA | 19.00 µA | 6.5 % |
| I<sub>C</sub> | 2.43 mA | 2.28 mA | 6.5 % |
| V<sub>CE</sub> | 7.56 V | 8.18 V | 7.5 % |
| V<sub>E</sub> | 2.43 V | 2.30 V | 5.7 % |
| V<sub>B</sub> | 3.13 V | 3.00 V | 4.3 % |

**Answer:**

- Exact: I<sub>C</sub> = 2.28 mA, V<sub>CE</sub> = 8.18 V, I<sub>B</sub> = 19.0 µA, V<sub>E</sub> = 2.30 V, V<sub>B</sub> = 3.00 V
- **Yes, the approximate approach is valid.** Every quantity differs by less than about 8 %, which is within normal engineering tolerance, and β itself varies far more than that between transistors. Since Eq. (4.33) was satisfied, the approximation is justified.

## Collector-Feedback Configuration

### Question 27 — Fig. 4.129

**Problem Type:** Collector-Feedback Bias (Type 4)

**Circuit values read from Fig. 4.129:** V<sub>CC</sub> = 16 V, R<sub>C</sub> = 3.6 kΩ, R<sub>F</sub> = 270 kΩ, R<sub>E</sub> = 1.2 kΩ, β = 120

**Given:**

- V<sub>CC</sub> = 16 V, R<sub>C</sub> = 3.6 kΩ, R<sub>F</sub> = 270 kΩ, R<sub>E</sub> = 1.2 kΩ, β = 120

**Find:**

- I<sub>B</sub>, I<sub>C</sub>, V<sub>C</sub>

**Formula:**

    I_B = (V_CC − 0.7)/[R_F + β(R_C + R_E)] ;  I_C = β I_B ;  V_C = V_CC − I_C R_C

**Solution:**

1. R<sub>C</sub> + R<sub>E</sub> = 3600 + 1200 = 4800 Ω
   β(R<sub>C</sub> + R<sub>E</sub>) = 120 × 4800 = 576 000 Ω

2. Denominator = 270 000 + 576 000 = 846 000 Ω
3. I<sub>B</sub> = (16 − 0.7) / 846 000 = 15.3 / 846 000 = **18.09 µA**
4. I<sub>C</sub> = 120 × 18.09 µA = **2.17 mA**
5. V<sub>C</sub> = 16 − (2.17 mA)(3.6 kΩ) = 16 − 7.81 = **8.19 V**

**Answer:**

- **(a)** I<sub>B</sub> = 18.09 µA  (b) I<sub>C</sub> = 2.17 mA  (c) V<sub>C</sub> = 8.19 V

---

### Question 29 — Fig. 4.130

**Problem Type:** Collector-Feedback (voltage-feedback) Bias (Type 4)

**Circuit values read from Fig. 4.130:** V<sub>CC</sub> = 30 V, R<sub>C</sub> = 8.2 kΩ, R<sub>E</sub> = 1.8 kΩ, feedback path = 330 kΩ + 220 kΩ in series, β = 180

**Given:**

- V<sub>CC</sub> = 30 V, R<sub>C</sub> = 8.2 kΩ, R<sub>E</sub> = 1.8 kΩ, β = 180
- The feedback path has 330 kΩ and 220 kΩ in series, with a 5 µF capacitor to ground at their junction

**Find:**

- I<sub>C</sub>, V<sub>C</sub>, V<sub>E</sub>, V<sub>CE</sub>

**Formula:**

    For DC, capacitors are OPEN → R_F = 330 kΩ + 220 kΩ = 550 kΩ
    I_B = (V_CC − 0.7)/[R_F + β(R_C + R_E)]

**Solution:**

1. All capacitors (10 µF, 5 µF) are open circuits for DC.
   The 5 µF to ground carries no DC current, so the two feedback resistors are simply in series:
   R<sub>F</sub> = 330 + 220 = **550 kΩ**

2. R<sub>C</sub> + R<sub>E</sub> = 8200 + 1800 = 10 000 Ω
   β(R<sub>C</sub> + R<sub>E</sub>) = 180 × 10 000 = 1 800 000 Ω

3. Denominator = 550 000 + 1 800 000 = 2 350 000 Ω
4. I<sub>B</sub> = (30 − 0.7) / 2 350 000 = 29.3 / 2 350 000 = 12.47 µA
5. I<sub>C</sub> = 180 × 12.47 µA = **2.24 mA**
6. V<sub>C</sub> = 30 − (2.244 mA)(8.2 kΩ) = 30 − 18.40 = **11.60 V**
7. V<sub>E</sub> = (2.244 mA)(1.8 kΩ) = **4.04 V**
8. V<sub>CE</sub> = 11.60 − 4.04 = **7.56 V**

**Answer:**

- **(a)** I<sub>C</sub> = 2.24 mA  (b) V<sub>C</sub> = 11.60 V  (c) V<sub>E</sub> = 4.04 V  (d) V<sub>CE</sub> = 7.56 V

---

### Question 33 — Fig. 4.133

**Problem Type:** Collector-Feedback → Reverse problem (Type 8)

**Circuit values read from Fig. 4.133:** V<sub>CC</sub> = 18 V, R<sub>C</sub> = 2.2 kΩ, R<sub>F</sub> = 330 kΩ, R<sub>E</sub> = 1.2 kΩ; β unknown, V<sub>B</sub> = 4 V given in the question

**Given:**

- V<sub>CC</sub> = 18 V, R<sub>C</sub> = 2.2 kΩ, R<sub>F</sub> = 330 kΩ, R<sub>E</sub> = 1.2 kΩ, V<sub>B</sub> = 4 V

**Find:**

- V<sub>E</sub>, I<sub>C</sub>, V<sub>C</sub>, V<sub>CE</sub>, I<sub>B</sub>, β

**Formula:**

    V_E = V_B − 0.7 ;  I_C ≈ I_E = V_E/R_E ;  V_C = V_CC − I_C R_C
    I_B = (V_C − V_B)/R_F ;  β = I_C/I_B

**Solution:**

1. V<sub>E</sub> = 4 − 0.7 = **3.3 V**
2. I<sub>E</sub> = 3.3 / 1.2 kΩ = 2.75 mA, so I<sub>C</sub> ≈ **2.75 mA**
3. V<sub>C</sub> = 18 − (2.75 mA)(2.2 kΩ) = 18 − 6.05 = **11.95 V**
4. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 11.95 − 3.3 = **8.65 V**
5. R<sub>F</sub> runs from the collector to the base, so the voltage across it is V<sub>C</sub> − V<sub>B</sub>:
   I<sub>B</sub> = (11.95 − 4) / 330 kΩ = 7.95 / 330 000 = **24.09 µA**

6. β = I<sub>C</sub>/I<sub>B</sub> = 2.75 mA / 24.09 µA = **114.2**

**Answer:**

- **(a)** V<sub>E</sub> = 3.3 V  (b) I<sub>C</sub> = 2.75 mA  (c) V<sub>C</sub> = 11.95 V
- **(d)** V<sub>CE</sub> = 8.65 V  (e) I<sub>B</sub> = 24.09 µA  (f) β = 114.2

## Emitter-Follower Configuration

### Question 34 — Fig. 4.134

**Problem Type:** Emitter Follower with split supply (Type 5)

**Circuit values read from Fig. 4.134:** +6 V top rail, R<sub>B</sub> = 330 kΩ to base, collector grounded, R<sub>E</sub> = 1.2 kΩ to a −6 V rail, β = 120

**Given:**

- Top supply +6 V, R<sub>B</sub> = 330 kΩ, R<sub>E</sub> = 1.2 kΩ, bottom supply −6 V, β = 120

**Find:**

- V<sub>E</sub> and I<sub>E</sub>

**Formula:**

    KVL base–emitter loop:
    V_top + |V_bottom| − 0.7 = I_B[R_B + (β+1)R_E]
    V_E = −|V_bottom| + I_E R_E

**Solution:**

1. Total driving voltage around the base loop = 6 + 6 − 0.7 = **11.3 V**
   (both supplies add, because the loop goes from +6 V down to −6 V)

2. Denominator = 330 000 + 121(1200) = 330 000 + 145 200 = 475 200 Ω
3. I<sub>B</sub> = 11.3 / 475 200 = 23.78 µA
4. I<sub>E</sub> = 121 × 23.78 µA = **2.877 mA**
5. V<sub>E</sub> is measured from ground. Starting at the −6 V rail and rising through R<sub>E</sub>:
   V<sub>E</sub> = −6 + (2.877 mA)(1.2 kΩ) = −6 + 3.45 = **−2.55 V**

**Answer:**

- I<sub>E</sub> = 2.877 mA, V<sub>E</sub> = −2.55 V

> **Watch out:** V<sub>E</sub> is negative here. The emitter sits below ground because the bottom rail is at −6 V.

---

### Question 35 — Fig. 4.135

**Problem Type:** Emitter Follower with voltage divider (Type 5)

**Circuit values read from Fig. 4.135:** V<sub>CC</sub> = 12 V, R<sub>1</sub> = 22 kΩ (top), R<sub>2</sub> = 82 kΩ (bottom), R<sub>E</sub> = 1.2 kΩ, collector tied straight to V<sub>CC</sub>, β = 110

**Given:**

- V<sub>CC</sub> = 12 V, R<sub>1</sub> = 22 kΩ, R<sub>2</sub> = 82 kΩ, R<sub>E</sub> = 1.2 kΩ, β = 110
- No R<sub>C</sub> — the collector connects directly to V<sub>CC</sub>

**Find:**

- **(a)** I<sub>B</sub>, I<sub>C</sub>, I<sub>E</sub>  (b) V<sub>B</sub>, V<sub>C</sub>, V<sub>E</sub>  (c) V<sub>BC</sub>, V<sub>CE</sub>

**Formula:**

    R_Th = R_1R_2/(R_1+R_2) ;  E_Th = V_CC R_2/(R_1+R_2)
    I_B = (E_Th − 0.7)/[R_Th + (β+1)R_E]

**Solution — part (a):**

1. R<sub>Th</sub> = (22 × 82)/(22 + 82) = 1804/104 = **17.35 kΩ**
2. E<sub>Th</sub> = 12 × 82/104 = 984/104 = **9.46 V**
3. Denominator = 17 346 + 111(1200) = 17 346 + 133 200 = 150 546 Ω
4. I<sub>B</sub> = (9.462 − 0.7) / 150 546 = 8.762 / 150 546 = **58.2 µA**
5. I<sub>C</sub> = 110 × 58.2 µA = **6.40 mA**
6. I<sub>E</sub> = 111 × 58.2 µA = **6.46 mA**

**Solution — part (b):**

7. V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub> = (6.46 mA)(1.2 kΩ) = **7.75 V**
8. V<sub>B</sub> = V<sub>E</sub> + 0.7 = **8.45 V**
9. V<sub>C</sub> = V<sub>CC</sub> = **12 V** (no R<sub>C</sub>, so no drop)

**Solution — part (c):**

10. V<sub>BC</sub> = V<sub>B</sub> − V<sub>C</sub> = 8.45 − 12 = **−3.55 V**
11. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 12 − 7.75 = **4.25 V**

**Answer:**

- **(a)** I<sub>B</sub> = 58.2 µA, I<sub>C</sub> = 6.40 mA, I<sub>E</sub> = 6.46 mA
- **(b)** V<sub>B</sub> = 8.45 V, V<sub>C</sub> = 12 V, V<sub>E</sub> = 7.75 V
- **(c)** V<sub>BC</sub> = −3.55 V, V<sub>CE</sub> = 4.25 V

> V<sub>BC</sub> is negative, which is exactly right — the base–collector junction must be reverse-biased in the active region.

## Common-Base Configuration

### Question 36 — Fig. 4.136

**Problem Type:** Common Base with split supply (Type 6)

**Circuit values read from Fig. 4.136:** +16 V through R<sub>C</sub> = 12 kΩ to the collector, base to ground through 9.1 kΩ, emitter through R<sub>E</sub> = 15 kΩ to −12 V, β = 80

**Given:**

- +16 V supply, R<sub>C</sub> = 12 kΩ, R<sub>B</sub> = 9.1 kΩ (base to ground), R<sub>E</sub> = 15 kΩ, −12 V supply, β = 80

**Find:**

- I<sub>B</sub>, I<sub>C</sub>, V<sub>CE</sub>, V<sub>C</sub>

**Formula:**

    KVL base–emitter loop (from ground, through R_B, the junction, R_E, to −12 V):
    12 − 0.7 = I_B[R_B + (β+1)R_E]

**Solution:**

1. Driving voltage in the base loop = 12 − 0.7 = **11.3 V**
2. Denominator = 9100 + 81(15 000) = 9100 + 1 215 000 = 1 224 100 Ω
3. I<sub>B</sub> = 11.3 / 1 224 100 = **9.23 µA**
4. I<sub>C</sub> = 80 × 9.23 µA = **0.739 mA**
5. I<sub>E</sub> = 81 × 9.23 µA = 0.748 mA
6. V<sub>C</sub> = 16 − (0.7385 mA)(12 kΩ) = 16 − 8.86 = **7.14 V**
7. V<sub>E</sub> = −12 + (0.7477 mA)(15 kΩ) = −12 + 11.22 = −0.78 V
8. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 7.14 − (−0.78) = **7.92 V**

**Answer:**

- **(a)** I<sub>B</sub> = 9.23 µA  (b) I<sub>C</sub> = 0.739 mA  (c) V<sub>CE</sub> = 7.92 V  (d) V<sub>C</sub> = 7.14 V

---

### Question 37 — Fig. 4.137

**Problem Type:** Common Base, base grounded (Type 6)

**Circuit values read from Fig. 4.137:** emitter through 2.2 kΩ to −8 V, base grounded, collector through 1.8 kΩ to +10 V. β is not given.

**Given:**

- R<sub>E</sub> = 2.2 kΩ to −8 V, base grounded, R<sub>C</sub> = 1.8 kΩ to +10 V

**Find:**

- I<sub>E</sub>, V<sub>C</sub>, V<sub>CE</sub>

**Formula:**

    V_E = V_B − 0.7 = −0.7 V  (base grounded)
    I_E = (V_E − V_EE)/R_E ;  I_C ≈ I_E ;  V_C = V_CC − I_C R_C

**Solution:**

1. Base is grounded, so V<sub>B</sub> = 0 and V<sub>E</sub> = 0 − 0.7 = **−0.7 V**
2. Voltage across R<sub>E</sub> = V<sub>E</sub> − (−8) = −0.7 + 8 = 7.3 V
   I<sub>E</sub> = 7.3 / 2.2 kΩ = **3.32 mA**

3. β is not given, so take I<sub>C</sub> ≈ I<sub>E</sub> = 3.32 mA
   V<sub>C</sub> = 10 − (3.318 mA)(1.8 kΩ) = 10 − 5.97 = **4.03 V**

4. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 4.03 − (−0.7) = **4.73 V**

**Answer:**

- **(a)** I<sub>E</sub> = 3.32 mA  (b) V<sub>C</sub> = 4.03 V  (c) V<sub>CE</sub> = 4.73 V

---

### Question 38 — Fig. 4.138

**Problem Type:** Common Base → Reverse problem (Types 6 + 8)

**Circuit values read from Fig. 4.138:** 14 V supply through R<sub>C</sub> (unknown) to the collector, V<sub>C</sub> = 8 V, base held at 4 V, R<sub>E</sub> = 1.1 kΩ to ground, β = 90

**Given:**

- V<sub>CC</sub> = 14 V, V<sub>C</sub> = 8 V, V<sub>B</sub> = 4 V, R<sub>E</sub> = 1.1 kΩ, β = 90

**Find:**

- **(a)** R<sub>C</sub>  (b) I<sub>B</sub> and I<sub>E</sub>  (c) V<sub>BC</sub> and V<sub>CE</sub>

**Formula:**

    V_E = V_B − 0.7 ;  I_E = V_E/R_E ;  I_B = I_E/(β+1) ;  I_C = β I_B
    R_C = (V_CC − V_C)/I_C

**Solution — part (a):**

1. V<sub>E</sub> = 4 − 0.7 = 3.3 V
2. I<sub>E</sub> = 3.3 / 1.1 kΩ = 3 mA
3. I<sub>B</sub> = 3 mA / 91 = 32.97 µA
   I<sub>C</sub> = 90 × 32.97 µA = 2.967 mA

4. Drop across R<sub>C</sub> = 14 − 8 = 6 V
   R<sub>C</sub> = 6 / 2.967 mA = **2.02 kΩ**

**Solution — part (b):**

5. I<sub>B</sub> = **32.97 µA**, I<sub>E</sub> = **3 mA**

**Solution — part (c):**

6. V<sub>BC</sub> = V<sub>B</sub> − V<sub>C</sub> = 4 − 8 = **−4 V**
7. V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub> = 8 − 3.3 = **4.7 V**

**Answer:**

- **(a)** R<sub>C</sub> = 2.02 kΩ  (b) I<sub>B</sub> = 32.97 µA, I<sub>E</sub> = 3 mA  (c) V<sub>BC</sub> = −4 V, V<sub>CE</sub> = 4.7 V

## Design Operations

### Question 41 — Fixed-bias design

**Problem Type:** Design → Fixed bias (Type 9)

**Given:**

- V<sub>CC</sub> = 12 V, β = 80, I<sub>CQ</sub> = 2.5 mA, V<sub>CEQ</sub> = 6 V

**Find:**

- R<sub>C</sub> and R<sub>B</sub>, rounded to standard values

**Formula:**

    R_C = (V_CC − V_CEQ)/I_CQ ;  I_B = I_CQ/β ;  R_B = (V_CC − 0.7)/I_B

**Solution:**

1. Voltage across R<sub>C</sub> = 12 − 6 = 6 V
   R<sub>C</sub> = 6 / 2.5 mA = 2.4 kΩ → standard value **2.4 kΩ** (exact match)

2. I<sub>B</sub> = 2.5 mA / 80 = 31.25 µA
3. R<sub>B</sub> = (12 − 0.7) / 31.25 µA = 11.3 / 31.25×10<sup>−6</sup> = 361.6 kΩ
   Nearest standard value: **360 kΩ**

**Answer:**

- R<sub>C</sub> = 2.4 kΩ (standard), R<sub>B</sub> = 361.6 kΩ → use **360 kΩ** (standard)

---

### Question 42 — Emitter-stabilized design

**Problem Type:** Design → Emitter bias (Type 9)

**Given:**

- V<sub>CC</sub> = 20 V, I<sub>Csat</sub> = 10 mA, β = 120, R<sub>C</sub> = 4R<sub>E</sub>
- Target: I<sub>CQ</sub> = ½I<sub>Csat</sub> and V<sub>CEQ</sub> = ½V<sub>CC</sub>

**Find:**

- R<sub>C</sub>, R<sub>E</sub>, R<sub>B</sub>

**Formula:**

    I_Csat = V_CC/(R_C + R_E)  →  R_C + R_E = V_CC/I_Csat
    R_B = (V_CC − 0.7 − V_E)/I_B

**Solution:**

1. Targets: I<sub>CQ</sub> = ½(10 mA) = **5 mA**, V<sub>CEQ</sub> = ½(20) = **10 V**
2. From saturation: R<sub>C</sub> + R<sub>E</sub> = 20 / 10 mA = 2000 Ω
3. With R<sub>C</sub> = 4R<sub>E</sub>: 4R<sub>E</sub> + R<sub>E</sub> = 5R<sub>E</sub> = 2000
   R<sub>E</sub> = **400 Ω** → nearest standard **390 Ω**
   R<sub>C</sub> = 4(400) = **1.6 kΩ** → standard **1.6 kΩ** (exact match)

4. Check: V<sub>CEQ</sub> = 20 − (5 mA)(2 kΩ) = 20 − 10 = 10 V ✓
5. I<sub>B</sub> = 5 mA / 120 = 41.67 µA
   I<sub>E</sub> = 121 × 41.67 µA = 5.042 mA
   V<sub>E</sub> = (5.042 mA)(400 Ω) = 2.02 V

6. R<sub>B</sub> = (20 − 0.7 − 2.02) / 41.67 µA = 17.28 / 41.67×10<sup>−6</sup> = 414.8 kΩ
   Nearest standard: **430 kΩ**

**Answer:**

- R<sub>E</sub> = 400 Ω → **390 Ω** (standard)
- R<sub>C</sub> = **1.6 kΩ** (standard)
- R<sub>B</sub> = 414.8 kΩ → **430 kΩ** (standard)

---

### Question 43 — Voltage-divider design

**Problem Type:** Design → Voltage-divider bias (Type 9)

**Given:**

- V<sub>CC</sub> = 24 V, β = 110, I<sub>CQ</sub> = 4 mA, V<sub>CEQ</sub> = 8 V, V<sub>E</sub> = ⅛V<sub>CC</sub>

**Find:**

- R<sub>E</sub>, R<sub>C</sub>, R<sub>1</sub>, R<sub>2</sub>

**Formula:**

    V_E = V_CC/8 ;  R_E = V_E/I_C ;  R_C = (V_CC − V_CEQ − V_E)/I_C
    R_2 ≤ βR_E/10 ;  R_1 = V_CC R_2/V_B − R_2

**Solution:**

1. V<sub>E</sub> = 24/8 = **3 V**
2. R<sub>E</sub> = 3 / 4 mA = **750 Ω** → standard **750 Ω** (exact match)
3. Voltage across R<sub>C</sub> = 24 − 8 − 3 = 13 V
   R<sub>C</sub> = 13 / 4 mA = 3.25 kΩ → nearest standard **3.3 kΩ**

4. V<sub>B</sub> = V<sub>E</sub> + 0.7 = **3.7 V**
5. Choose R<sub>2</sub> using Eq. (4.33): R<sub>2</sub> ≤ βR<sub>E</sub>/10 = (110 × 750)/10 = 8250 Ω
   Pick standard **R<sub>2</sub> = 8.2 kΩ** (just under the limit)

6. R<sub>1</sub> + R<sub>2</sub> = V<sub>CC</sub>R<sub>2</sub>/V<sub>B</sub> = (24 × 8200)/3.7 = 196 800/3.7 = 53.19 kΩ
   R<sub>1</sub> = 53.19 − 8.2 = 44.99 kΩ → nearest standard **43 kΩ**
   (47 kΩ is almost equally close; either is defensible — state which you chose.)

**Answer:**

- R<sub>E</sub> = **750 Ω**, R<sub>C</sub> = 3.25 kΩ → **3.3 kΩ**, R<sub>2</sub> = **8.2 kΩ**, R<sub>1</sub> = 44.99 kΩ → **43 kΩ**

## Current Source Circuits

### Question 51 — Fig. 4.147

**Problem Type:** Current source, fixed base supply (Type 10)

**Circuit values read from Fig. 4.147:** 28 V through a 2.2 kΩ load to the collector, base fed from +6 V through R<sub>B</sub> = 100 kΩ, R<sub>E</sub> = 1.2 kΩ to ground, β = 120

**Given:**

- Load = 2.2 kΩ (from 28 V to the collector), base supply +6 V, R<sub>B</sub> = 100 kΩ, R<sub>E</sub> = 1.2 kΩ, β = 120

**Find:**

- The current through the 2.2 kΩ load

**Formula:**

    I_B = (6 − 0.7)/[R_B + (β+1)R_E] ;  I = I_C = β I_B

**Solution:**

1. Denominator = 100 000 + 121(1200) = 100 000 + 145 200 = 245 200 Ω
2. I<sub>B</sub> = (6 − 0.7) / 245 200 = 5.3 / 245 200 = 21.62 µA
3. I = I<sub>C</sub> = 120 × 21.62 µA = **2.59 mA**
4. Check the transistor is active: V<sub>C</sub> = 28 − (2.594 mA)(2.2 kΩ) = 28 − 5.71 = 22.29 V,
   V<sub>E</sub> = (2.615 mA)(1.2 kΩ) = 3.14 V → V<sub>CE</sub> = 19.15 V, comfortably active ✓

**Answer:**

- Current through the 2.2 kΩ load = **2.59 mA**

> The load value never entered the calculation — that is the defining feature of a current source.

---

### Question 52 — Fig. 4.148

**Problem Type:** Current source with a resistor divider (Type 10)

**Circuit values read from Fig. 4.148:** base divider of 4.3 kΩ (to ground) and 4.3 kΩ (to −18 V), R<sub>E</sub> = 1.8 kΩ to −18 V, β = 100

**Given:**

- Base divider: 4.3 kΩ from base to ground, 4.3 kΩ from base to −18 V
- R<sub>E</sub> = 1.8 kΩ to −18 V, β = 100

**Find:**

- The current I

**Formula:**

    R_Th = 4.3k ∥ 4.3k ;  E_Th = divider between 0 V and −18 V
    I_B = (E_Th − V_EE − 0.7)/[R_Th + (β+1)R_E]

**Solution:**

1. The divider sits between 0 V and −18 V with two equal resistors, so the base sits halfway:
   E<sub>Th</sub> = −18 × 4.3/(4.3 + 4.3) = **−9 V**

2. R<sub>Th</sub> = (4.3 × 4.3)/(4.3 + 4.3) = **2.15 kΩ**
3. Base loop driving voltage = E<sub>Th</sub> − V<sub>EE</sub> − 0.7 = −9 − (−18) − 0.7 = **8.3 V**
4. Denominator = 2150 + 101(1800) = 2150 + 181 800 = 183 950 Ω
5. I<sub>B</sub> = 8.3 / 183 950 = 45.12 µA
6. I = I<sub>C</sub> = 100 × 45.12 µA = **4.51 mA**

**Answer:**

- I = 4.51 mA

> Using the quick approximation (ignoring I<sub>B</sub>): V<sub>E</sub> = −9.7 V, I<sub>E</sub> = 8.3/1.8 kΩ = 4.61 mA. That is about 2 % off — the exact answer 4.51 mA is preferred.

---

### Question 53 — Fig. 4.149

**Problem Type:** Zener-controlled current source (Type 10)

**Circuit values read from Fig. 4.149:** base held by a 5.1 V Zener referenced to −12 V, 1.5 kΩ from the base node to ground, R<sub>E</sub> = 1.2 kΩ to −12 V, β = 200

**Given:**

- V<sub>Z</sub> = 5.1 V (between the base and the −12 V rail), R<sub>E</sub> = 1.2 kΩ, V<sub>EE</sub> = −12 V, β = 200

**Find:**

- The current I

**Formula:**

    V_B = V_EE + V_Z   (Zener fixes the base voltage directly)
    V_E = V_B − 0.7 ;  I_E = (V_E − V_EE)/R_E ;  I = I_C = β/(β+1) × I_E

**Solution:**

1. The Zener pins the base 5.1 V above the −12 V rail:
   V<sub>B</sub> = −12 + 5.1 = **−6.9 V**

2. V<sub>E</sub> = −6.9 − 0.7 = **−7.6 V**
3. Voltage across R<sub>E</sub> = V<sub>E</sub> − (−12) = −7.6 + 12 = 4.4 V
   I<sub>E</sub> = 4.4 / 1.2 kΩ = **3.67 mA**

4. I = I<sub>C</sub> = αI<sub>E</sub> = (200/201)(3.667 mA) = **3.65 mA**

**Answer:**

- I = 3.65 mA

> The 1.5 kΩ resistor only supplies the Zener's bias current — it does not appear in the load-current calculation.

<div class="pagebreak"></div>

# Chapter 1 — Semiconductor Diodes

### Question 15

**Problem Type:** (a) Thermal voltage (Type 1); (b) Diode current from Shockley's equation (Type 2)

**Given:**

- **(a)** T = 20 °C
- **(b)** I<sub>s</sub> = 40 nA, n = 2, V<sub>D</sub> = 0.5 V, same temperature

**Find:**

- **(a)** V<sub>T</sub>  (b) I<sub>D</sub>

**Formula:**

    T_K = T_C + 273 ;  V_T = (8.62 × 10^−5) T_K
    I_D = I_s (e^(V_D/(nV_T)) − 1)

**Solution — part (a):**

1. T<sub>K</sub> = 20 + 273 = 293 K
2. V<sub>T</sub> = (8.62 × 10<sup>−5</sup>)(293) = 0.02525 V ≈ **25.27 mV**

**Solution — part (b):**

3. nV<sub>T</sub> = 2 × 0.02527 = 0.05054 V
4. Exponent = V<sub>D</sub>/(nV<sub>T</sub>) = 0.5 / 0.05054 = 9.893
5. e<sup>9.893</sup> = 19 785
6. I<sub>D</sub> = (40 × 10<sup>−9</sup>)(19 785 − 1) = (40 × 10<sup>−9</sup>)(19 784) = 7.91 × 10<sup>−4</sup> A

**Answer:**

- **(a)** V<sub>T</sub> = 25.27 mV
- **(b)** I<sub>D</sub> = 0.791 mA

---

### Question 16

**Problem Type:** Thermal voltage + diode current at a new temperature (Types 1 + 2)

> **Value flagged:** your document states "I<sub>s</sub> has increased to **5.0 mA**". A reverse saturation current of 5 mA is extremely large for a diode (typical values are nA to µA), so this looks like a "µ" that was lost when the text was copied. **I have not assumed either way — both answers are below.** Use whichever matches your question paper.

**Given:**

- T = 100 °C, n = 2, V<sub>D</sub> = 0.5 V, I<sub>s</sub> = 5.0 mA (as written) or 5.0 µA (if the µ was lost)

**Find:**

- V<sub>T</sub> and I<sub>D</sub>

**Formula:**

    V_T = (8.62 × 10^−5) T_K ;  I_D = I_s (e^(V_D/(nV_T)) − 1)

**Solution:**

1. T<sub>K</sub> = 100 + 273 = 373 K
2. V<sub>T</sub> = (8.62 × 10<sup>−5</sup>)(373) = 0.03215 V ≈ **32.17 mV**
3. nV<sub>T</sub> = 2 × 0.03217 = 0.06434 V
4. Exponent = 0.5 / 0.06434 = 7.771
5. e<sup>7.771</sup> = 2370.6
6. **If I<sub>s</sub> = 5.0 mA (as written):**
   I<sub>D</sub> = (5 × 10<sup>−3</sup>)(2369.6) = **11.85 A**

7. **If I<sub>s</sub> = 5.0 µA:**
   I<sub>D</sub> = (5 × 10<sup>−6</sup>)(2369.6) = **11.85 mA**

**Answer:**

- V<sub>T</sub> = 32.17 mV
- I<sub>D</sub> = **11.85 A** using the value as written (5.0 mA), or **11.85 mA** if I<sub>s</sub> is 5.0 µA
- The method and every intermediate number are identical; only the final multiplier changes.

---

### Question 17

**Problem Type:** Reverse-bias diode current (Type 3)

> **Value flagged:** your document states "I<sub>s</sub> **0.1 mA**". As in Q16, this is likely 0.1 µA. Fortunately the *method* and the *form* of the answer are unaffected — the answer is simply −I<sub>s</sub>, whatever its value.

**Given:**

- T = 20 °C, silicon diode, n = 2, I<sub>s</sub> = 0.1 mA (as written), V<sub>D</sub> = −10 V

**Find:**

- **(a)** I<sub>D</sub>  (b) Is the result expected? Why?

**Formula:**

    I_D = I_s (e^(V_D/(nV_T)) − 1)

**Solution — part (a):**

1. V<sub>T</sub> at 20 °C = 25.27 mV (from Q15), so nV<sub>T</sub> = 0.05054 V
2. Exponent = −10 / 0.05054 = **−197.9**
3. e<sup>−197.9</sup> ≈ 1.2 × 10<sup>−86</sup> — effectively **zero**
4. I<sub>D</sub> = I<sub>s</sub>(0 − 1) = **−I<sub>s</sub> = −0.1 mA** (or −0.1 µA if I<sub>s</sub> is in µA)

**Solution — part (b):**

5. **Yes, this is exactly what we expect.** Under reverse bias the exponential term collapses to zero, so the equation reduces to I<sub>D</sub> = −I<sub>s</sub>. The diode blocks, and only the tiny reverse saturation (leakage) current flows, in the reverse direction. The minus sign just shows the direction is opposite to normal forward conduction.
6. Note also that the answer does **not** depend on how large the reverse voltage is — anything past about −0.5 V gives the same result. That is why the reverse characteristic is drawn as a flat horizontal line.

**Answer:**

- **(a)** I<sub>D</sub> = −I<sub>s</sub> = −0.1 mA (as written)
- **(b)** Yes — expected. The exponential term vanishes under reverse bias, leaving only the reverse saturation current.

---

### Question 18

**Problem Type:** Find I<sub>s</sub> from a known I<sub>D</sub> (Type 4)

**Given:**

- I<sub>D</sub> = 8 mA, n = 1, V<sub>D</sub> = 0.5 V, T = 25 °C (room temperature)

**Find:**

- I<sub>s</sub>

**Formula:**

    I_s = I_D / (e^(V_D/(nV_T)) − 1)

**Solution:**

1. T<sub>K</sub> = 25 + 273 = 298 K
2. V<sub>T</sub> = (8.62 × 10<sup>−5</sup>)(298) = 0.02569 V ≈ 25.70 mV
3. n = 1, so nV<sub>T</sub> = 0.02570 V
4. Exponent = 0.5 / 0.02570 = 19.453
5. e<sup>19.453</sup> = 2.809 × 10<sup>8</sup>
6. I<sub>s</sub> = (8 × 10<sup>−3</sup>) / (2.809 × 10<sup>8</sup> − 1) = 2.85 × 10<sup>−11</sup> A

**Answer:**

- I<sub>s</sub> = 2.85 × 10<sup>−11</sup> A = **28.5 pA**

> A picoamp-scale answer is exactly what you should expect. If you get milliamps, you divided the wrong way round.

---

### Question 19

**Problem Type:** Find V<sub>D</sub> from a known I<sub>D</sub> (Type 5)

**Given:**

- I<sub>D</sub> = 6 mA, V<sub>T</sub> = 26 mV (given directly), n = 1, I<sub>s</sub> = 1 nA

**Find:**

- V<sub>D</sub>

**Formula:**

    V_D = n V_T ln(I_D/I_s + 1)

**Solution:**

1. I<sub>D</sub>/I<sub>s</sub> = (6 × 10<sup>−3</sup>) / (1 × 10<sup>−9</sup>) = 6 × 10<sup>6</sup>
2. Add 1: 6 000 001 ≈ 6 × 10<sup>6</sup> (the +1 is negligible here)
3. ln(6 × 10<sup>6</sup>) = **15.607**
4. V<sub>D</sub> = (1)(0.026)(15.607) = 0.4058 V

**Answer:**

- V<sub>D</sub> = **0.406 V**

> Sanity check: 0.406 V is a believable forward voltage for a diode. Use **ln**, not log₁₀ — log₁₀ would give 0.176 V, which is wrong.

<div class="pagebreak"></div>

# Chapter 2 — Diode Applications

## Series Diode Configurations

### Question 5 — Fig. 2.155

**Problem Type:** Series diode circuits → ON/OFF test (Types 1, 2)

> **Note on Fig. 2.155(a):** the first digit of the battery label is cut off at the left edge of the image in your document (it reads "…2 V"). **This does not change the answer** — the diode is reverse-biased regardless of the magnitude, so I = 0 A either way.

**Circuit values read from Fig. 2.155:**

- **(a)** Battery with **− at the top, + at the bottom (grounded)**, Si diode pointing right, 10 Ω
- **(b)** 10 Ω branch, Si diode pointing right, a second Si diode with its cathode at the top node in series with 20 Ω to ground, and a 20 V battery (− left, + right) whose + side is grounded
- **(c)** 10 V battery (+ top, − bottom grounded), two Si diodes in the middle branch pointing in **opposite** directions, 10 Ω on the right

**Find:**

- The current I in each configuration

**Formula:**

    Check diode direction first. If reverse-biased → I = 0.
    Otherwise:  I = (driving voltage − ΣV_K)/ΣR

**Solution — (a):**

1. The battery has **−** on top and **+** at the bottom, and the bottom is grounded.
   So the top node = −(battery value), i.e. it is **negative**.

2. The diode's anode faces that negative node; its cathode side reaches ground through the 10 Ω.
3. Anode is more negative than the cathode → the diode is **reverse-biased**.
4. Therefore **I = 0 A**.

**Solution — (b):**

5. The 20 V battery has + grounded and − at the top node, so the top node A sits at **−20 V**.
6. Both Si diodes point **toward** node A (the horizontal one from the 10 Ω branch, the vertical one from the 20 Ω branch), so both are forward-biased: current flows from ground, up through the resistors, into node A, and back through the battery.
7. Left branch: the node above the 10 Ω sits at V<sub>A</sub> + 0.7 = −20 + 0.7 = −19.3 V
   I₁ = (0 − (−19.3)) / 10 = **1.93 A**

8. Middle branch: the node above the 20 Ω also sits at −19.3 V
   I₂ = (0 − (−19.3)) / 20 = **0.965 A**

9. The marked I is the total returning through the battery:
   I = I₁ + I₂ = 1.93 + 0.965 = **2.90 A**

**Solution — (c):**

10. The two Si diodes in the middle branch point in **opposite** directions (one conducts down, the other only up).
11. Opposing diodes in series → that branch is an **open circuit**, no current can flow through it.
12. What remains is simply the 10 V battery across the 10 Ω:
    I = 10 / 10 = **1 A**

**Answer:**

- **(a)** I = **0 A** (diode reverse-biased)
- **(b)** I = **2.90 A** (1.93 A through the 10 Ω + 0.965 A through the 20 Ω)
- **(c)** I = **1 A** (middle branch is dead)

---

### Question 6 — Fig. 2.156

**Problem Type:** Series diode circuit → find V<sub>o</sub> and I<sub>D</sub> (Type 1)

**Circuit values read from Fig. 2.156:**

- **(a)** −5 V source, Si diode with its **cathode facing the −5 V side**, output node, 2.2 kΩ to ground
- **(b)** +8 V, 1.2 kΩ, output node, 4.7 kΩ, Si diode pointing down, −6 V

**Given / Find:**

- V<sub>o</sub> and I<sub>D</sub> for each network

**Formula:**

    I = (ΣV − ΣV_K)/ΣR ;  V_o from the node voltages

**Solution — (a):**

1. The diode's cathode is at −5 V and its anode is at the output node, so current flows **from the output node toward the −5 V source** (right to left), matching the I<sub>D</sub> arrow.
2. The diode is forward-biased. Across it: V<sub>anode</sub> − V<sub>cathode</sub> = 0.7
   V<sub>o</sub> − (−5) = 0.7 → V<sub>o</sub> = **−4.3 V**

3. Current through the 2.2 kΩ (from ground down to V<sub>o</sub>):
   I<sub>D</sub> = (0 − (−4.3)) / 2.2 kΩ = 4.3 / 2200 = **1.96 mA**

**Solution — (b):**

4. Top is +8 V, bottom is −6 V, and the diode points downward → forward-biased.
5. Total driving voltage = 8 − (−6) = 14 V; subtract the diode drop: 14 − 0.7 = 13.3 V
6. Total resistance = 1.2 kΩ + 4.7 kΩ = 5.9 kΩ
   I<sub>D</sub> = 13.3 / 5900 = **2.25 mA**

7. V<sub>o</sub> = 8 − I<sub>D</sub>(1.2 kΩ) = 8 − (2.254 mA)(1200) = 8 − 2.70 = **5.30 V**

**Answer:**

- **(a)** V<sub>o</sub> = −4.3 V, I<sub>D</sub> = 1.96 mA
- **(b)** V<sub>o</sub> = 5.30 V, I<sub>D</sub> = 2.25 mA

---

### Question 7 — Fig. 2.157

**Problem Type:** Series diode circuit with mixed materials (Type 1)

**Circuit values read from Fig. 2.157:**

- **(a)** 12 V, Si diode, Ge diode (both pointing right), 2 kΩ, output node, 10 kΩ to ground
- **(b)** +10 V, 1.2 kΩ, Si diode pointing right, output node, 4.7 kΩ, then a **+10 V** source at the bottom

**Given / Find:**

- V<sub>o</sub> for each network

**Formula:**

    I = (V − V_K(Si) − V_K(Ge))/ΣR ;  V_o = I × R

**Solution — (a):**

1. Both diodes point the same way and the 12 V drives them forward → both conduct.
2. Total diode drop = 0.7 (Si) + 0.3 (Ge) = **1.0 V**
3. I = (12 − 1.0) / (2 kΩ + 10 kΩ) = 11 / 12 000 = **0.917 mA**
4. V<sub>o</sub> = I × 10 kΩ = (0.9167 mA)(10 000) = **9.17 V**

**Solution — (b):**

5. **Test the diode first.** Assume it is off: no current flows, so there is no drop across either resistor.
   Then the left of the diode sits at 10 V and the right (output node) sits at 10 V — from the bottom source.

6. Voltage across the diode = 10 − 10 = **0 V**, which is less than 0.7 V → the diode is **OFF**.
7. Confirm by assuming it is on: KVL gives 10 − I(1.2 k) − 0.7 − I(4.7 k) − 10 = 0 → I = −0.119 mA.
   A negative current contradicts the diode's direction, so it really is off.

8. With no current, there is no drop across the 4.7 kΩ, so V<sub>o</sub> = the bottom source = **10 V**

**Answer:**

- **(a)** V<sub>o</sub> = 9.17 V
- **(b)** V<sub>o</sub> = 10 V (diode off — the two 10 V sources cancel, leaving nothing to forward-bias it)

---

### Question 9 — Fig. 2.159

**Problem Type:** (a) Series diodes with two outputs; (b) opposing diodes (Types 1, 2)

**Circuit values read from Fig. 2.159:**

- **(a)** +12 V, Si diode pointing right, node V<sub>o1</sub>, 4.7 kΩ, node V<sub>o2</sub>, GaAs diode pointing down to ground
- **(b)** −10 V, Ge diode pointing right, Si diode with its **cathode on the left** (i.e. pointing left), node V<sub>o1</sub>, 1.2 kΩ, node V<sub>o2</sub>, 3.3 kΩ to ground

**Given / Find:**

- V<sub>o1</sub> and V<sub>o2</sub> for each network

**Formula:**

    (a) I = (V − V_K(Si) − V_K(GaAs))/R
    (b) Opposing diodes → open circuit → I = 0

**Solution — (a):**

1. Both diodes are forward-biased by the +12 V.
2. V<sub>o1</sub> is right after the Si diode: V<sub>o1</sub> = 12 − 0.7 = **11.3 V**
3. V<sub>o2</sub> is across the GaAs diode to ground, so it equals that diode's drop:
   V<sub>o2</sub> = **1.2 V**

4. Check with the current: I = (12 − 0.7 − 1.2)/4.7 kΩ = 10.1/4700 = 2.15 mA
   and V<sub>o1</sub> − V<sub>o2</sub> = 11.3 − 1.2 = 10.1 V across the 4.7 kΩ ✓

**Solution — (b):**

5. The Ge diode points **right** (anode at the −10 V side); the Si diode points **left** (cathode on the left).
   They face in **opposite** directions.

6. Opposing diodes in series → **open circuit**, I = 0.
7. With no current, there is no drop across the 3.3 kΩ or the 1.2 kΩ, and both output nodes are tied to ground through those resistors:
   V<sub>o2</sub> = **0 V**, and V<sub>o1</sub> = V<sub>o2</sub> = **0 V**

**Answer:**

- **(a)** V<sub>o1</sub> = 11.3 V, V<sub>o2</sub> = 1.2 V
- **(b)** V<sub>o1</sub> = 0 V, V<sub>o2</sub> = 0 V (back-to-back diodes block in both directions)

---

### Question 13 — Fig. 2.163

**Problem Type:** Parallel diode branches → KCL at the output node (Type 3)

**Circuit values read from Fig. 2.163:** +10 V feeding two parallel branches — an upper branch with a Si diode and 2 kΩ, a lower branch with a GaAs diode and 2 kΩ — joining at node V<sub>o</sub>, which has a 2 kΩ to ground

**Given:**

- V = 10 V, Si branch: 0.7 V + 2 kΩ; GaAs branch: 1.2 V + 2 kΩ; load 2 kΩ to ground

**Find:**

- V<sub>o</sub> and I<sub>D</sub> (the current in the Si branch, as marked)

**Formula:**

    Assume both ON, then KCL at V_o:
    (10 − 0.7 − V_o)/2k + (10 − 1.2 − V_o)/2k = V_o/2k

**Solution:**

1. Assume both diodes conduct. Write KCL at the output node (current in = current out):
   (10 − 0.7 − V<sub>o</sub>)/2k + (10 − 1.2 − V<sub>o</sub>)/2k = V<sub>o</sub>/2k

2. All resistors are 2 kΩ, so multiply through by 2k:
   (9.3 − V<sub>o</sub>) + (8.8 − V<sub>o</sub>) = V<sub>o</sub>

3. 18.1 − 2V<sub>o</sub> = V<sub>o</sub> → 18.1 = 3V<sub>o</sub>
4. V<sub>o</sub> = 18.1/3 = **6.03 V**
5. Si branch (this is the marked I<sub>D</sub>):
   I<sub>D</sub> = (9.3 − 6.033)/2 kΩ = 3.267/2000 = **1.63 mA**

6. **Check both assumptions:** GaAs branch = (8.8 − 6.033)/2 kΩ = 1.38 mA. Both currents are positive, so both diodes really do conduct ✓
7. Check KCL: 1.63 + 1.38 = 3.02 mA = V<sub>o</sub>/2k = 6.033/2000 = 3.02 mA ✓

**Answer:**

- V<sub>o</sub> = **6.03 V**, I<sub>D</sub> (Si branch) = **1.63 mA**
- (The GaAs branch carries 1.38 mA — both branches conduct because each has its own series resistor.)

## Sinusoidal Inputs; Half-Wave Rectification

### Question 22 — Fig. 2.168

**Problem Type:** Half-wave rectifier, ideal diode → find V<sub>m</sub> and sketch (Type 4)

**Circuit values read from Fig. 2.168:** v<sub>i</sub> → ideal diode → output node → 2 kΩ to ground; the measured DC level is V<sub>dc</sub> = 2 V

**Given:**

- Ideal diode, R = 2 kΩ, f = 60 Hz, V<sub>dc</sub> = 2 V

**Find:**

- The peak value of v<sub>i</sub>, and sketches of v<sub>i</sub>, v<sub>d</sub>, i<sub>d</sub>

**Formula:**

    V_dc = 0.318 V_m   →   V_m = V_dc / 0.318
    T = 1/f

**Solution:**

1. Work backwards from the DC level:
   V<sub>m</sub> = 2 / 0.318 = **6.29 V**

2. Period: T = 1/60 = **16.67 ms**, so each half-cycle lasts 8.33 ms
3. Peak diode current: i<sub>d(peak)</sub> = 6.29 / 2 kΩ = **3.14 mA**

**Sketches — what to draw:**

| Waveform | Positive half-cycle (diode ON) | Negative half-cycle (diode OFF) |
|---|---|---|
| **v<sub>i</sub>** | sine rising to +6.29 V | sine falling to −6.29 V |
| **v<sub>d</sub>** (across diode) | **0 V** (ideal diode = short) | follows v<sub>i</sub> down to **−6.29 V** |
| **i<sub>d</sub>** | half-sine peaking at **3.14 mA** | **0 mA** |

**Answer:**

- Peak value of v<sub>i</sub> = **6.29 V**
- v<sub>d</sub> = 0 during the positive half; v<sub>d</sub> = v<sub>i</sub> (down to −6.29 V) during the negative half
- i<sub>d</sub> = positive half-sine with a 3.14 mA peak, zero for the other half; T = 16.67 ms

> **The classic mistake:** drawing v<sub>d</sub> as zero everywhere. When the diode is OFF no current flows, so the **entire input appears across the diode**.

---

### Question 23 — Fig. 2.168 with a silicon diode

**Problem Type:** Half-wave rectifier with V<sub>K</sub> = 0.7 V (Type 4)

**Given:**

- Same circuit, but a silicon diode (V<sub>K</sub> = 0.7 V), V<sub>dc</sub> = 2 V, R = 2 kΩ, f = 60 Hz

**Find:**

- Peak value of v<sub>i</sub>, and the same three sketches

**Formula:**

    V_dc = 0.318 (V_m − 0.7)   →   V_m = V_dc/0.318 + 0.7

**Solution:**

1. V<sub>m</sub> − 0.7 = 2 / 0.318 = 6.29 V
2. V<sub>m</sub> = 6.29 + 0.7 = **6.99 V ≈ 7.0 V**
3. Peak output voltage = V<sub>m</sub> − 0.7 = **6.29 V**
4. Peak current = 6.29 / 2 kΩ = **3.14 mA**

**Sketches — what changes from Q22:**

| Waveform | Positive half-cycle | Negative half-cycle |
|---|---|---|
| **v<sub>i</sub>** | up to +6.99 V | down to −6.99 V |
| **v<sub>d</sub>** | held at **+0.7 V** (not 0) | follows v<sub>i</sub> to **−6.99 V** |
| **i<sub>d</sub>** | half-sine, peak 3.14 mA, but **conducts only while v<sub>i</sub> > 0.7 V** | 0 mA |

**Answer:**

- Peak value of v<sub>i</sub> = **6.99 V**
- v<sub>d</sub> = 0.7 V when conducting, and reaches −6.99 V when off
- i<sub>d</sub> peak = 3.14 mA; conduction is slightly **less than** a full half-cycle because the diode waits for v<sub>i</sub> to exceed 0.7 V

---

### Question 24 — Fig. 2.169 (10 kΩ load added)

**Problem Type:** Half-wave rectifier with a parallel load (Type 4)

**Circuit values read from Fig. 2.169:** v<sub>i</sub> → ideal diode → output node, with 2 kΩ and R<sub>L</sub> = 10 kΩ **both** to ground

**Given:**

- Repeat Q22 (ideal diode, V<sub>m</sub> = 6.29 V, f = 60 Hz), now with R<sub>L</sub> = 10 kΩ in parallel with the 2 kΩ

**Find:**

- Sketch v<sub>L</sub> and i<sub>L</sub>

**Formula:**

    R_parallel = (2k × 10k)/(2k + 10k)
    Diode ON → v_L = v_i ;  i_L = v_L/R_L

**Solution:**

1. Parallel resistance = (2 × 10)/(2 + 10) kΩ = 20/12 = **1.667 kΩ**
2. The ideal diode connects v<sub>i</sub> straight to the output node with no series resistor, so during the positive half-cycle the output simply follows the input:
   v<sub>L(peak)</sub> = V<sub>m</sub> = **6.29 V**

3. Negative half-cycle: diode off → v<sub>L</sub> = **0 V**
4. Load current: i<sub>L(peak)</sub> = 6.29 / 10 kΩ = **0.629 mA**
5. Total diode current: i<sub>d(peak)</sub> = 6.29 / 1.667 kΩ = **3.77 mA**
6. DC level across the load: V<sub>L(dc)</sub> = 0.318 × 6.29 = **2 V** (unchanged)
   I<sub>L(dc)</sub> = 2 / 10 kΩ = **0.2 mA**

**Sketches — what to draw:**

| Waveform | Positive half-cycle | Negative half-cycle |
|---|---|---|
| **v<sub>L</sub>** | half-sine up to **6.29 V** | **0 V** |
| **i<sub>L</sub>** | half-sine up to **0.629 mA** | **0 mA** |

**Answer:**

- v<sub>L</sub> = half-wave rectified sine, peak **6.29 V**, DC level **2 V**
- i<sub>L</sub> = half-wave rectified, peak **0.629 mA**, DC level **0.2 mA**
- Adding the load does not change the output **voltage** shape (the ideal diode has no series resistance); it only increases the total current the diode must carry, from 3.14 mA to **3.77 mA**.

## Full-Wave Rectification

### Question 29 — Fig. 2.173

**Problem Type:** Full-wave bridge rectifier (Type 5)

**Circuit values read from Fig. 2.173:** standard four-diode bridge, **ideal diodes**, v<sub>i</sub> peak = 100 V, R<sub>L</sub> = 2.2 kΩ

**Given:**

- Bridge rectifier, ideal diodes, V<sub>m</sub> = 100 V, R<sub>L</sub> = 2.2 kΩ

**Find:**

- v<sub>o</sub>, the PIV rating of each diode, and the maximum current through each diode

**Formula:**

    V_o(peak) = V_m − 2V_K = V_m  (ideal)
    V_dc = 0.636 V_o(peak)
    PIV(bridge) = V_m
    I_max = V_o(peak)/R_L

**Solution:**

1. Diodes are ideal, so no drops are subtracted:
   v<sub>o</sub> = full-wave rectified sine with peak **100 V**

2. DC level: V<sub>dc</sub> = 0.636 × 100 = **63.6 V**
3. PIV: when a diode is off in a bridge, it must block the full peak:
   PIV = V<sub>m</sub> = **100 V**

4. Maximum diode current = peak load current (each diode carries the full load current during its half-cycle):
   I<sub>max</sub> = 100 / 2.2 kΩ = **45.45 mA**

**Answer:**

- v<sub>o</sub> = full-wave rectified sine, peak **100 V**, V<sub>dc</sub> = **63.6 V**
- PIV of each diode = **100 V**
- Maximum current through each diode = **45.45 mA**

---

### Question 30 — Fig. 2.174

**Problem Type:** Bridge with two arms replaced by resistors (Type 5, variant)

**Circuit values read from Fig. 2.174:** a bridge whose **top two arms are ideal diodes** and whose **bottom two arms are 2.2 kΩ resistors**; output taken across a 2.2 kΩ load to ground; v<sub>i</sub> peak = 100 V

**Given:**

- V<sub>m</sub> = 100 V, ideal diodes, all three resistors = 2.2 kΩ

**Find:**

- Sketch v<sub>o</sub> and determine the available DC voltage

**Formula:**

    Analyse each half-cycle separately with the conducting diode replaced by a short.

**Solution:**

1. **Positive half-cycle.** The diode from the top node to the output node conducts (ideal → a short); the other diode is reverse-biased and off.
2. Label the output node R and the source's lower node B. With the diode shorted, the source voltage appears directly between R and B.
   From R there are two return paths to B: the 2.2 kΩ bridge arm directly, and the 2.2 kΩ load to ground then the other 2.2 kΩ arm up to B.

3. Writing KCL at both nodes and using the fact that all three resistors are equal gives V<sub>R</sub> = −V<sub>B</sub>, and since V<sub>R</sub> − V<sub>B</sub> = v<sub>i</sub>:
   2V<sub>R</sub> = v<sub>i</sub> → **v<sub>o</sub> = v<sub>i</sub>/2**

4. **Negative half-cycle.** Now the other diode conducts, tying the top node to ground, and the analysis mirrors itself:
   v<sub>o</sub> = |v<sub>i</sub>|/2

5. So the output is a **full-wave rectified sine of half the input amplitude**:
   v<sub>o(peak)</sub> = 100/2 = **50 V**

6. V<sub>dc</sub> = 0.636 × 50 = **31.8 V**

**Sketch — what to draw:**

- A full-wave rectified sine (both humps positive), peak **50 V**, twice the input frequency.

**Answer:**

- v<sub>o</sub> = full-wave rectified sine with peak **50 V**
- Available DC voltage = **31.8 V**

> The resistors split the source voltage in half, so this circuit delivers half the DC output of the true bridge in Q29.

## Clippers

> Your document lists the "Clippers" heading with the note *"how understand its clippers circuit"* and no typed question text — the actual questions are inside the images. They are **Problem 33 (Fig. 2.177)** and **Problem 35 (Fig. 2.179)**, both solved below.

### Question 33 — Fig. 2.177

**Problem Type:** Series clipper, square-wave input (Type 6)

**Circuit values read from Fig. 2.177:** input is a square wave switching between **+12 V and −12 V**

- **(a)** v<sub>i</sub> → Si diode (pointing right) → 2.2 kΩ → node v<sub>o</sub> → 1.8 kΩ to ground
- **(b)** v<sub>i</sub> → Si diode (pointing right) → 4 V battery (**− on the left, + on the right**) → node v<sub>o</sub> → 10 kΩ to ground

**Given / Find:**

- v<sub>o</sub> for each network, at both input levels

**Formula:**

    Diode ON  → I = (v_i − V_K ± V_battery)/ΣR ,  v_o from Ohm's law
    Diode OFF → I = 0 → v_o = 0 (series clipper, no current in the output resistor)

**Solution — (a):**

1. **When v<sub>i</sub> = +12 V:** the diode is forward-biased.
   I = (12 − 0.7) / (2.2 kΩ + 1.8 kΩ) = 11.3 / 4000 = 2.825 mA
   v<sub>o</sub> = I × 1.8 kΩ = (2.825 mA)(1800) = **5.09 V**

2. **When v<sub>i</sub> = −12 V:** the anode is negative → diode **OFF**.
   No current flows, so there is no drop across the 1.8 kΩ:
   v<sub>o</sub> = **0 V**

**Solution — (b):**

3. **When v<sub>i</sub> = +12 V:** assume the diode conducts.
   Walking from the input: V<sub>cathode</sub> = 12 − 0.7 = 11.3 V.
   The battery has − on the left and + on the right, so crossing it **raises** the potential by 4 V:
   v<sub>o</sub> = 11.3 + 4 = **15.3 V**
   Check: current = 15.3/10 kΩ = 1.53 mA, positive and in the diode's direction ✓

4. **When v<sub>i</sub> = −12 V:** assume off. With no current, v<sub>o</sub> = 0 V, so the cathode sits at 0 − 4 = −4 V.
   The anode is at −12 V, well below the cathode → **reverse-biased**, confirmed off.
   v<sub>o</sub> = **0 V**

**Answer:**

| v<sub>i</sub> | (a) v<sub>o</sub> | (b) v<sub>o</sub> |
|---|---|---|
| +12 V | **5.09 V** | **15.3 V** |
| −12 V | **0 V** | **0 V** |

> In (b) the battery **adds** to the output because its + terminal faces the output node. Reverse the battery and you would get 12 − 0.7 − 4 = 7.3 V instead.

---

### Question 35 — Fig. 2.179

**Problem Type:** Parallel (shunt) clipper with a DC source (Type 6)

**Circuit values read from Fig. 2.179:** input is a **sine wave of ±8 V**

- **(a)** v<sub>i</sub> → 1 kΩ → node v<sub>o</sub>; from v<sub>o</sub> down to the bottom rail: a Si diode (anode at the top) in series with a 4 V battery (**+ on top**)
- **(b)** v<sub>i</sub> → 2.2 kΩ → 3 V battery (**+ on the left, − on the right**) → node v<sub>o</sub>; from v<sub>o</sub> a Si diode (anode at the top) down to ground

**Given / Find:**

- v<sub>o</sub> for each network

**Formula:**

    Clipping level = walk from v_o down the diode branch to ground, adding V_K and the battery
    Diode ON  → v_o = clipping level
    Diode OFF → no branch current → v_o follows the input path

**Solution — (a):**

1. Walk down the branch from v<sub>o</sub>: through the diode (+0.7 V) then to the battery's + terminal (+4 V).
   **Clipping level = 4 + 0.7 = 4.7 V**

2. **While v<sub>i</sub> < 4.7 V:** the diode is off, the branch carries no current, so there is no drop across the 1 kΩ:
   v<sub>o</sub> = **v<sub>i</sub>**

3. **While v<sub>i</sub> > 4.7 V:** the diode conducts and holds the node:
   v<sub>o</sub> = **4.7 V** (flat)

4. The negative peak is untouched: v<sub>o</sub> reaches **−8 V**.

**Sketch (a):** a sine wave whose **top is flattened at +4.7 V**, negative peak still −8 V.

**Solution — (b):**

5. **Diode branch:** the diode's anode is at v<sub>o</sub>, cathode at ground → it conducts when v<sub>o</sub> tries to exceed +0.7 V.
   **Clipping level = 0.7 V**

6. **When the diode is off:** no current flows, so no drop across the 2.2 kΩ. The 3 V battery has + on the left and − on the right, so crossing it toward the output **lowers** the potential by 3 V:
   v<sub>o</sub> = **v<sub>i</sub> − 3**

7. **Turn-on point:** the diode conducts once v<sub>i</sub> − 3 ≥ 0.7, i.e. once **v<sub>i</sub> ≥ 3.7 V**.
   Above that: v<sub>o</sub> = **0.7 V** (flat)

8. At the negative peak: v<sub>o</sub> = −8 − 3 = **−11 V**

**Sketch (b):** a sine wave **shifted down 3 V** and **flattened at +0.7 V** on top; negative peak −11 V.

**Answer:**

- **(a)** v<sub>o</sub> = v<sub>i</sub> for v<sub>i</sub> ≤ 4.7 V, clipped flat at **4.7 V** above that; negative peak **−8 V**
- **(b)** v<sub>o</sub> = v<sub>i</sub> − 3 for v<sub>i</sub> < 3.7 V, clipped flat at **0.7 V** above that; negative peak **−11 V**

## Clampers

> As with the clippers, your document's "Clampers" heading has no typed question text — the questions are in the images. They are **Problem 38 (Fig. 2.182)**, **Problem 39 (Fig. 2.183)**, **Problem 40 (Fig. 2.184)** and **Problem 41 (Fig. 2.185)**, all solved below.

### Question 38 — Fig. 2.182

**Problem Type:** Clamper analysis (Type 7)

**Circuit values read from Fig. 2.182:** input is a **sine wave of ±120 V**

- **(a)** series C → node v<sub>o</sub>, with an **ideal diode whose cathode is at the top** (so it conducts upward, from ground into the node) in parallel with R
- **(b)** series C → node v<sub>o</sub>, with an **ideal diode whose anode is at the top** in series with **E = 20 V (+ on top)**, in parallel with R

**Given / Find:**

- Sketch v<sub>o</sub> for each

**Formula:**

    During conduction: v_o = clamping level, and  V_C = v_i − v_o
    Diode off:  v_o = v_i − V_C
    Check: v_o(p-p) must equal v_i(p-p) = 240 V

**Solution — (a):**

1. The diode's cathode faces the output node, so it conducts whenever v<sub>o</sub> tries to go **below 0 V**. Ideal → clamping level = **0 V**.
2. This happens during the **negative** half-cycle. At the negative peak, v<sub>i</sub> = −120 V and v<sub>o</sub> = 0:
   V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub> = −120 − 0 = **−120 V**
   (i.e. the capacitor holds 120 V with its **right** plate positive)

3. During the positive half-cycle the diode is off, and V<sub>C</sub> is held:
   v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub> = v<sub>i</sub> + 120

4. At the positive peak: v<sub>o</sub> = 120 + 120 = **+240 V**
   At the negative peak: v<sub>o</sub> = −120 + 120 = **0 V**

5. **Check:** peak-to-peak = 240 − 0 = 240 V = input peak-to-peak ✓

**Sketch (a):** the input sine shifted **up by 120 V**, swinging from **0 V to +240 V**. This is a **positive clamper**.

**Solution — (b):**

6. The diode's anode faces the output node and its cathode goes to the + terminal of the 20 V source, so it conducts whenever v<sub>o</sub> tries to rise **above 20 V**. Ideal → clamping level = **+20 V**.
7. This happens during the **positive** half-cycle. At the positive peak, v<sub>i</sub> = +120 V and v<sub>o</sub> = 20 V:
   V<sub>C</sub> = 120 − 20 = **+100 V** (left plate positive)

8. During the negative half-cycle the diode is off:
   v<sub>o</sub> = v<sub>i</sub> − 100

9. At the negative peak: v<sub>o</sub> = −120 − 100 = **−220 V**
10. **Check:** peak-to-peak = 20 − (−220) = 240 V ✓

**Sketch (b):** the input sine shifted **down by 100 V**, swinging from **+20 V to −220 V**. This is a **negative clamper with a 20 V reference**.

**Answer:**

- **(a)** v<sub>o</sub> swings from **0 V to +240 V** (V<sub>C</sub> = 120 V)
- **(b)** v<sub>o</sub> swings from **+20 V to −220 V** (V<sub>C</sub> = 100 V)

---

### Question 39 — Fig. 2.183

**Problem Type:** (a),(b) Time-constant check (Type 9); (c) Clamper sketch (Type 7)

**Circuit values read from Fig. 2.183:** input is a **square wave of ±12 V at f = 1 kHz**; C = 0.1 µF; a **Si diode with its anode at the top** in series with a **2 V battery (− on top, + at the bottom rail)**; R = 56 kΩ in parallel with the output

**Given:**

- C = 0.1 µF, R = 56 kΩ, f = 1 kHz, v<sub>i</sub> = ±12 V square wave, Si diode

**Find:**

- **(a)** 5τ  (b) compare with half the period  (c) sketch v<sub>o</sub>

**Formula:**

    τ = RC ;  T = 1/f ;  clamping level from the diode branch ;  V_C = v_i − v_o

**Solution — part (a):**

1. τ = RC = (56 × 10<sup>3</sup>)(0.1 × 10<sup>−6</sup>) = 5.6 × 10<sup>−3</sup> s = 5.6 ms
2. 5τ = 5 × 5.6 ms = **28 ms**

**Solution — part (b):**

3. T = 1/f = 1/1000 = 1 ms, so **T/2 = 0.5 ms**
4. Compare: 28 ms vs 0.5 ms → **5τ is 56 times larger than the half period**
5. Because 5τ ≫ T/2, the capacitor has almost no time to discharge during a half-cycle. Its voltage stays essentially constant, so the clamping action is very good and the output holds a flat top.

**Solution — part (c):**

6. **Clamping level.** The battery has its − terminal at the top, so the diode's cathode sits at 0 − 2 = −2 V.
   The diode conducts when v<sub>o</sub> ≥ −2 + 0.7 = **−1.3 V**.

7. **During v<sub>i</sub> = +12 V:** the diode conducts and holds the node at v<sub>o</sub> = **−1.3 V**
   V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub> = 12 − (−1.3) = **13.3 V**

8. **During v<sub>i</sub> = −12 V:** the diode is off and V<sub>C</sub> is held:
   v<sub>o</sub> = −12 − 13.3 = **−25.3 V**

9. **Check:** peak-to-peak = −1.3 − (−25.3) = 24 V = input peak-to-peak (12 + 12) ✓

**Sketch (c):** a square wave alternating between **−1.3 V** and **−25.3 V**, with the flat top at −1.3 V lasting 0.5 ms and the bottom at −25.3 V lasting 0.5 ms.

**Answer:**

- **(a)** 5τ = **28 ms**
- **(b)** T/2 = **0.5 ms**; 5τ is **56× larger**, so the capacitor barely discharges and clamping is excellent
- **(c)** v<sub>o</sub> is a square wave between **−1.3 V and −25.3 V** (V<sub>C</sub> = 13.3 V)

---

### Question 40 — Fig. 2.184

**Problem Type:** Clamper design, ideal diodes (Type 8)

**Waveforms read from Fig. 2.184:**

- Input: square wave between **+20 V and −20 V** (40 V peak-to-peak)
- Required output: square wave between **+30 V and −10 V** (40 V peak-to-peak)
- Ideal diodes

**Given / Find:**

- Design the clamper — determine the DC source and the diode orientation

**Formula:**

    Shift = v_o − v_i  (must match at both levels)
    Clamping level = the held level ;  V_battery = clamping level ∓ V_K
    Design rule: 5RC ≫ T/2

**Solution:**

1. **Check the swing:** input p-p = 20 − (−20) = 40 V; output p-p = 30 − (−10) = 40 V ✓
   A clamper can do this (it shifts without changing the swing).

2. **Find the shift:**
   +20 V → +30 V: shift = **+10 V**
   −20 V → −10 V: shift = **+10 V** ✓ consistent
   So we need a **positive shift of 10 V**.

3. **Identify the clamped level.** The output's lower level, **−10 V**, is the one the diode must hold.
4. **Capacitor voltage.** During the negative half (v<sub>i</sub> = −20 V), the diode conducts and v<sub>o</sub> = −10 V:
   V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub> = −20 − (−10) = **−10 V** (right plate positive)

5. **Verify the other half.** With the diode off: v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub> = 20 − (−10) = **+30 V** ✓
6. **Circuit design:**
   - A capacitor **C in series** with the input.
   - A shunt branch from the output node to ground: an **ideal diode with its cathode facing the output node** (so it conducts upward, into the node, when v<sub>o</sub> falls) in series with a **10 V DC source whose negative terminal faces the diode** (so the diode's anode sits at −10 V).
   - Ideal diode → V<sub>K</sub> = 0, so the clamping level = the source voltage = **−10 V** ✓
   - A resistor **R in parallel** with the diode branch.
7. **Component sizing:** the frequency is **not given** in Fig. 2.184, so exact R and C values cannot be pinned down. State the design condition instead:
   **5RC ≫ T/2**, where T = 1/f of the input. (For example, if f were 1 kHz, then T/2 = 0.5 ms and R = 100 kΩ with C = 1 µF would give 5RC = 500 ms, comfortably satisfying the rule.)

**Answer:**

- **Series capacitor C**, plus a shunt branch containing an **ideal diode (cathode toward the output node)** in series with a **10 V DC source (negative terminal toward the diode)**, and **R in parallel**.
- This clamps the lower level at −10 V and produces V<sub>C</sub> = 10 V, giving an output of +30 V / −10 V.
- Choose R and C so that **5RC ≫ T/2**. The frequency is not stated in the figure, so no numerical R and C can be determined from the given information.

---

### Question 41 — Fig. 2.185

**Problem Type:** Clamper design, silicon diodes (Type 8)

**Waveforms read from Fig. 2.185:**

- Input: square wave between **+10 V and −10 V** (20 V peak-to-peak)
- Required output: square wave between **+2.7 V and −17.3 V** (20 V peak-to-peak)
- Silicon diodes (V<sub>K</sub> = 0.7 V)

**Given / Find:**

- Design the clamper

**Formula:**

    Shift = v_o − v_i ;  clamping level = V_battery + V_K  (for a diode with its anode at the output node)

**Solution:**

1. **Check the swing:** input p-p = 20 V; output p-p = 2.7 − (−17.3) = 20 V ✓
2. **Find the shift:**
   +10 V → +2.7 V: shift = **−7.3 V**
   −10 V → −17.3 V: shift = **−7.3 V** ✓ consistent
   So we need a **negative shift of 7.3 V**.

3. **Identify the clamped level.** The output's upper level, **+2.7 V**, is the one held flat.
4. **Capacitor voltage.** During the positive half (v<sub>i</sub> = +10 V), the diode conducts and v<sub>o</sub> = +2.7 V:
   V<sub>C</sub> = 10 − 2.7 = **+7.3 V** (left plate positive)

5. **Verify the other half.** Diode off: v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub> = −10 − 7.3 = **−17.3 V** ✓
6. **Find the DC source.** The diode's anode is at the output node and its cathode goes to the source. When conducting:
   v<sub>o</sub> = V<sub>source</sub> + V<sub>K</sub>
   2.7 = V<sub>source</sub> + 0.7 → **V<sub>source</sub> = 2 V**

7. **Circuit design:**
   - A capacitor **C in series** with the input.
   - A shunt branch from the output node to ground: a **silicon diode with its anode facing the output node**, in series with a **2 V DC source whose positive terminal faces the diode**.
   - A resistor **R in parallel**.
8. **Component sizing:** again the frequency is **not given** in Fig. 2.185, so state the condition **5RC ≫ T/2** rather than inventing numbers.

**Answer:**

- **Series capacitor C**, plus a shunt branch containing a **silicon diode (anode toward the output node)** in series with a **2 V DC source (positive terminal toward the diode)**, and **R in parallel**.
- Clamping level = 2 + 0.7 = **2.7 V** ✓, giving V<sub>C</sub> = 7.3 V and an output of +2.7 V / −17.3 V.
- Choose R and C so that **5RC ≫ T/2**. The frequency is not stated in the figure.

> **Compare Q40 and Q41:** in Q40 the diode's **cathode** faces the output (clamping the bottom, shifting up); in Q41 the **anode** faces the output (clamping the top, shifting down). That single reversal is what sets the direction of the shift.

## Zener Diodes

### Question 42 — Fig. 2.186

**Problem Type:** Zener regulator with variable R<sub>L</sub> (Type 10)

**Circuit values read from Fig. 2.186:** V<sub>i</sub> = 20 V, R<sub>S</sub> = 220 Ω, V<sub>Z</sub> = 10 V, P<sub>Zmax</sub> = 400 mW, R<sub>L</sub> variable

**Given:**

- V<sub>i</sub> = 20 V, R<sub>S</sub> = 220 Ω, V<sub>Z</sub> = 10 V, P<sub>Zmax</sub> = 400 mW

**Find:**

- **(a)** V<sub>L</sub>, I<sub>L</sub>, I<sub>Z</sub>, I<sub>R</sub> for R<sub>L</sub> = 180 Ω
- **(b)** the same for R<sub>L</sub> = 470 Ω
- **(c)** R<sub>L</sub> for maximum Zener power
- **(d)** minimum R<sub>L</sub> to keep the Zener on

**Formula:**

    Test:  V = V_i R_L/(R_S + R_L)   compare with V_Z
    Zener ON:  V_L = V_Z ;  I_R = (V_i − V_Z)/R_S ;  I_L = V_Z/R_L ;  I_Z = I_R − I_L
    I_Zmax = P_Zmax/V_Z ;  R_Lmin = R_S V_Z/(V_i − V_Z)

**Solution — part (a), R<sub>L</sub> = 180 Ω:**

1. **Test:** V = 20 × 180/(220 + 180) = 3600/400 = **9 V**
2. 9 V < V<sub>Z</sub> = 10 V → the **Zener is OFF**. It is just a voltage divider.
3. V<sub>L</sub> = **9 V**
4. I<sub>L</sub> = 9 / 180 = **50 mA**
5. I<sub>Z</sub> = **0 mA**
6. I<sub>R</sub> = I<sub>L</sub> = **50 mA**

**Solution — part (b), R<sub>L</sub> = 470 Ω:**

7. **Test:** V = 20 × 470/(220 + 470) = 9400/690 = **13.62 V**
8. 13.62 V > 10 V → the **Zener is ON**.
9. V<sub>L</sub> = **10 V**
10. I<sub>R</sub> = (20 − 10)/220 = 10/220 = **45.45 mA**
11. I<sub>L</sub> = 10/470 = **21.28 mA**
12. I<sub>Z</sub> = 45.45 − 21.28 = **24.17 mA**
13. Power check: P<sub>Z</sub> = 10 × 24.17 mA = 242 mW < 400 mW ✓ safe

**Solution — part (c), R<sub>L</sub> for maximum Zener power:**

14. I<sub>Zmax</sub> = P<sub>Zmax</sub>/V<sub>Z</sub> = 400 mW / 10 V = **40 mA**
15. With the Zener on, I<sub>R</sub> is fixed at 45.45 mA.
16. I<sub>L</sub> = I<sub>R</sub> − I<sub>Zmax</sub> = 45.45 − 40 = **5.45 mA**
17. R<sub>L</sub> = V<sub>Z</sub>/I<sub>L</sub> = 10 / 5.45 mA = **1.83 kΩ**

**Solution — part (d), minimum R<sub>L</sub>:**

18. R<sub>Lmin</sub> = R<sub>S</sub>V<sub>Z</sub>/(V<sub>i</sub> − V<sub>Z</sub>) = (220 × 10)/(20 − 10) = 2200/10 = **220 Ω**

**Answer:**

- **(a)** V<sub>L</sub> = 9 V, I<sub>L</sub> = 50 mA, I<sub>Z</sub> = 0 mA, I<sub>R</sub> = 50 mA (**Zener off**)
- **(b)** V<sub>L</sub> = 10 V, I<sub>L</sub> = 21.28 mA, I<sub>Z</sub> = 24.17 mA, I<sub>R</sub> = 45.45 mA (**Zener on**)
- **(c)** R<sub>L</sub> = **1.83 kΩ** gives maximum Zener power
- **(d)** R<sub>Lmin</sub> = **220 Ω**

> Part (a) is the trap: R<sub>L</sub> = 180 Ω is **below** the 220 Ω minimum found in part (d), which is exactly why the Zener cannot turn on.

---

### Question 43 — Fig. 2.187

**Problem Type:** Zener design (Type 12)

**Circuit values read from Fig. 2.187:** V<sub>i</sub> = 16 V, R<sub>S</sub> unknown, Zener with V<sub>Z</sub> unknown, R<sub>L</sub> variable

**Given:**

- V<sub>i</sub> = 16 V, required V<sub>L</sub> = 12 V, load current I<sub>L</sub> varies from **0 mA to 200 mA**

**Find:**

- **(a)** R<sub>S</sub> and V<sub>Z</sub>  (b) P<sub>Zmax</sub>

**Formula:**

    V_Z = V_L
    R_S = (V_i − V_Z)/I_L(max)
    Worst case for the Zener is I_L = 0 → I_Z = I_R
    P_Zmax = V_Z × I_R

**Solution — part (a):**

1. The Zener sets the output, so **V<sub>Z</sub> = V<sub>L</sub> = 12 V**
2. Size R<sub>S</sub> at the **heaviest** load, I<sub>L</sub> = 200 mA (this is when the Zener has the least current to spare, so set I<sub>Z</sub> ≈ 0):
   I<sub>R</sub> = I<sub>L(max)</sub> = 200 mA

3. Voltage across R<sub>S</sub> = 16 − 12 = 4 V
   R<sub>S</sub> = 4 / 200 mA = **20 Ω**

**Solution — part (b):**

4. The Zener's worst case is the **lightest** load, I<sub>L</sub> = 0 mA. Then it must absorb the entire I<sub>R</sub>:
   I<sub>Z</sub> = I<sub>R</sub> = (16 − 12)/20 = **200 mA**

5. P<sub>Zmax</sub> = V<sub>Z</sub> × I<sub>Z</sub> = 12 × 0.2 = **2.4 W**

**Answer:**

- **(a)** R<sub>S</sub> = **20 Ω**, V<sub>Z</sub> = **12 V**
- **(b)** P<sub>Zmax</sub> = **2.4 W** (the Zener must be rated for at least this)

> Note the opposite extremes: **R<sub>S</sub> is sized at maximum load**, but the **Zener's power rating is set by minimum load**.

---

### Question 44 — Fig. 2.188

**Problem Type:** Zener regulator → range of V<sub>i</sub> (Type 11)

**Circuit values read from Fig. 2.188:** R<sub>S</sub> = 91 Ω, V<sub>Z</sub> = 8 V, P<sub>Zmax</sub> = 400 mW, R<sub>L</sub> = 0.22 kΩ = 220 Ω

**Given:**

- R<sub>S</sub> = 91 Ω, V<sub>Z</sub> = 8 V, P<sub>Zmax</sub> = 400 mW, R<sub>L</sub> = 220 Ω (fixed)

**Find:**

- The range of V<sub>i</sub> that maintains V<sub>L</sub> = 8 V without exceeding the Zener's power rating

**Formula:**

    I_L = V_Z/R_L   (fixed)
    I_Zmax = P_Zmax/V_Z
    V_i(min) = V_Z + I_L R_S            (I_Z = 0)
    V_i(max) = V_Z + (I_L + I_Zmax) R_S  (I_Z = I_Zmax)

**Solution:**

1. R<sub>L</sub> is fixed and V<sub>L</sub> is held at 8 V, so the load current never changes:
   I<sub>L</sub> = 8 / 220 = **36.36 mA**

2. I<sub>Zmax</sub> = P<sub>Zmax</sub>/V<sub>Z</sub> = 400 mW / 8 V = **50 mA**
3. **Minimum V<sub>i</sub>** — the Zener is just barely on, so I<sub>Z</sub> = 0 and I<sub>R</sub> = I<sub>L</sub> = 36.36 mA:
   V<sub>i(min)</sub> = 8 + (36.36 mA)(91 Ω) = 8 + 3.31 = **11.31 V**

4. **Maximum V<sub>i</sub>** — the Zener is at its power limit, so I<sub>R</sub> = I<sub>L</sub> + I<sub>Zmax</sub> = 36.36 + 50 = 86.36 mA:
   V<sub>i(max)</sub> = 8 + (86.36 mA)(91 Ω) = 8 + 7.86 = **15.86 V**

**Answer:**

- **11.31 V ≤ V<sub>i</sub> ≤ 15.86 V**
- Below 11.31 V the Zener drops out of regulation and V<sub>L</sub> falls below 8 V; above 15.86 V the Zener exceeds its 400 mW rating.

<div class="pagebreak"></div>

# FINAL EXAM QUICK REVISION

## 1. Chapter → Problem Type

| Chapter | Problem Type | How to Recognize | Main Formula |
|---|---|---|---|
| 4 | Fixed bias — Q-point | One R<sub>B</sub>, emitter grounded | I<sub>B</sub> = (V<sub>CC</sub>−0.7)/R<sub>B</sub> |
| 4 | Emitter bias — Q-point | R<sub>B</sub> to V<sub>CC</sub> **plus** R<sub>E</sub> | I<sub>B</sub> = (V<sub>CC</sub>−0.7)/[R<sub>B</sub>+(β+1)R<sub>E</sub>] |
| 4 | Voltage divider — exact | Two base resistors R<sub>1</sub>, R<sub>2</sub> | R<sub>Th</sub>, E<sub>Th</sub>, then I<sub>B</sub> = (E<sub>Th</sub>−0.7)/[R<sub>Th</sub>+(β+1)R<sub>E</sub>] |
| 4 | Voltage divider — approx. | βR<sub>E</sub> ≥ 10R<sub>2</sub> holds | V<sub>B</sub> = V<sub>CC</sub>R<sub>2</sub>/(R<sub>1</sub>+R<sub>2</sub>) |
| 4 | Collector feedback | R<sub>F</sub> from base to **collector** | I<sub>B</sub> = (V<sub>CC</sub>−0.7)/[R<sub>F</sub>+β(R<sub>C</sub>+R<sub>E</sub>)] |
| 4 | Emitter follower | No R<sub>C</sub>, output at emitter | Same as emitter bias; V<sub>C</sub> = V<sub>CC</sub> |
| 4 | Common base | Base grounded / fixed V<sub>B</sub> | V<sub>E</sub> = V<sub>B</sub>−0.7, then I<sub>E</sub> = ΔV/R<sub>E</sub> |
| 4 | Saturation current | Word "I<sub>Csat</sub>" | I<sub>Csat</sub> = V<sub>CC</sub>/(R<sub>C</sub>+R<sub>E</sub>) |
| 4 | Reverse problem | Letters on resistors, numbers on nodes | Rearrange; start where V and I are both known |
| 4 | Design | "Design…", "Use standard values" | R = V<sub>across</sub>/I<sub>through</sub>, then round |
| 4 | Current source | "Calculate the current I" | Find V<sub>B</sub> → V<sub>E</sub> → I<sub>E</sub> → I<sub>C</sub> |
| 1 | Thermal voltage | Temperature in °C given | V<sub>T</sub> = (8.62×10<sup>−5</sup>)(T<sub>C</sub>+273) |
| 1 | Diode current | I<sub>s</sub>, n, positive V<sub>D</sub> | I<sub>D</sub> = I<sub>s</sub>(e<sup>V<sub>D</sub>/nV<sub>T</sub></sup>−1) |
| 1 | Reverse bias | Negative V<sub>D</sub> | I<sub>D</sub> = −I<sub>s</sub> |
| 1 | Find I<sub>s</sub> | "find I<sub>s</sub>" | I<sub>s</sub> = I<sub>D</sub>/(e<sup>V<sub>D</sub>/nV<sub>T</sub></sup>−1) |
| 1 | Find V<sub>D</sub> | "find the applied voltage" | V<sub>D</sub> = nV<sub>T</sub> ln(I<sub>D</sub>/I<sub>s</sub>+1) |
| 2 | Series diode | One loop, diodes + resistors | Check ON/OFF, then I = (ΣV−ΣV<sub>K</sub>)/ΣR |
| 2 | Opposing diodes | Arrows facing each other | Open circuit → I = 0 |
| 2 | Parallel diode branches | Two diode branches meeting | KCL at the output node |
| 2 | Half-wave rectifier | One diode + sine | V<sub>dc</sub> = 0.318(V<sub>m</sub>−V<sub>K</sub>) |
| 2 | Bridge rectifier | Four diodes in a diamond | V<sub>dc</sub> = 0.636V<sub>m</sub>, PIV = V<sub>m</sub> |
| 2 | Clipper | Diode across output, no capacitor | Clipping level = V<sub>batt</sub> + V<sub>K</sub> |
| 2 | Clamper | **Capacitor in series** | V<sub>C</sub> = v<sub>i</sub>−v<sub>o</sub>, then v<sub>o</sub> = v<sub>i</sub>−V<sub>C</sub> |
| 2 | Clamper design | Two waveforms shown | Find the shift and the clamped level |
| 2 | Zener, variable R<sub>L</sub> | Zener across a load | Test V = V<sub>i</sub>R<sub>L</sub>/(R<sub>S</sub>+R<sub>L</sub>) first |
| 2 | Zener, range of V<sub>i</sub> | R<sub>L</sub> fixed, "range of V<sub>i</sub>" | I<sub>Z</sub> = 0 and I<sub>Z</sub> = I<sub>Zmax</sub> |
| 2 | Zener design | "Design… maintain V<sub>L</sub> at…" | R<sub>S</sub> at max load; P<sub>Z</sub> at min load |

## 2. Formula Checklist

Tick these off before the exam. If you can write all of these from memory, you can do every question in this guide.

**Chapter 4 — must know**

- [ ] I<sub>C</sub> = βI<sub>B</sub>, I<sub>E</sub> = (β+1)I<sub>B</sub>, α = β/(β+1)
- [ ] V<sub>B</sub> = V<sub>E</sub> + 0.7, V<sub>CE</sub> = V<sub>C</sub> − V<sub>E</sub>
- [ ] Fixed bias: I<sub>B</sub> = (V<sub>CC</sub> − 0.7)/R<sub>B</sub>
- [ ] Emitter bias: I<sub>B</sub> = (V<sub>CC</sub> − 0.7)/[R<sub>B</sub> + (β+1)R<sub>E</sub>]
- [ ] Thévenin: R<sub>Th</sub> = R<sub>1</sub>∥R<sub>2</sub>, E<sub>Th</sub> = V<sub>CC</sub>R<sub>2</sub>/(R<sub>1</sub>+R<sub>2</sub>)
- [ ] Eq. (4.33): βR<sub>E</sub> ≥ 10R<sub>2</sub>
- [ ] Collector feedback: I<sub>B</sub> = (V<sub>CC</sub> − 0.7)/[R<sub>F</sub> + β(R<sub>C</sub>+R<sub>E</sub>)]
- [ ] I<sub>Csat</sub> = V<sub>CC</sub>/(R<sub>C</sub> + R<sub>E</sub>)
- [ ] Divider reverse: I<sub>1</sub> = I<sub>2</sub> + I<sub>B</sub>

**Chapter 1 — must know**

- [ ] V<sub>T</sub> = (8.62 × 10<sup>−5</sup>)(T<sub>C</sub> + 273)
- [ ] I<sub>D</sub> = I<sub>s</sub>(e<sup>V<sub>D</sub>/(nV<sub>T</sub>)</sup> − 1)
- [ ] V<sub>D</sub> = nV<sub>T</sub> ln(I<sub>D</sub>/I<sub>s</sub> + 1)
- [ ] Reverse bias → I<sub>D</sub> = −I<sub>s</sub>

**Chapter 2 — must know**

- [ ] V<sub>K</sub>: Ideal 0, Ge 0.3, Si 0.7, GaAs 1.2
- [ ] I = (ΣV − ΣV<sub>K</sub>)/ΣR
- [ ] Half-wave: V<sub>dc</sub> = 0.318(V<sub>m</sub> − V<sub>K</sub>)
- [ ] Full-wave: V<sub>dc</sub> = 0.636V<sub>m</sub>, PIV = V<sub>m</sub>
- [ ] Clipping level = V<sub>battery</sub> + V<sub>K</sub>
- [ ] Clamper: V<sub>C</sub> = v<sub>i</sub> − v<sub>o</sub> during conduction; then v<sub>o</sub> = v<sub>i</sub> − V<sub>C</sub>
- [ ] Zener test: V = V<sub>i</sub>R<sub>L</sub>/(R<sub>S</sub>+R<sub>L</sub>)
- [ ] I<sub>Z</sub> = I<sub>R</sub> − I<sub>L</sub>, I<sub>Zmax</sub> = P<sub>Zmax</sub>/V<sub>Z</sub>
- [ ] R<sub>Lmin</sub> = R<sub>S</sub>V<sub>Z</sub>/(V<sub>i</sub> − V<sub>Z</sub>)

## 3. "When I See This → Do This"

**Chapter 4**

- If you see **only one resistor at the base and the emitter grounded** → fixed bias → I<sub>B</sub> = (V<sub>CC</sub>−0.7)/R<sub>B</sub>
- If you see **R<sub>E</sub> anywhere** → the base-loop denominator becomes R<sub>B</sub> + (β+1)R<sub>E</sub>
- If you see **two resistors at the base** → find R<sub>Th</sub> and E<sub>Th</sub> first → then treat it as emitter bias
- If the question says **"approximate approach"** → first check βR<sub>E</sub> ≥ 10R<sub>2</sub>, then read V<sub>B</sub> straight off the divider
- If the base resistor **ends at the collector** → use β(R<sub>C</sub>+R<sub>E</sub>), not (β+1)R<sub>E</sub>
- If you see a **capacitor** in a DC bias problem → treat it as an **open circuit**; series resistors around it simply add
- If you see **no R<sub>C</sub>** → V<sub>C</sub> = V<sub>CC</sub> immediately
- If the **base is grounded** → V<sub>E</sub> = −0.7 V immediately, then use Ohm's law
- If you see **two supplies (+V and −V)** → the base-loop driving voltage is V<sub>top</sub> + |V<sub>bottom</sub>| − 0.7
- If the question asks for **I<sub>Csat</sub>** → just V<sub>CC</sub> ÷ (R<sub>C</sub> + R<sub>E</sub>); ignore β entirely
- If **resistors are labelled with letters** and node voltages are given → reverse problem → start at a resistor where you know both V and I
- If you are finding **R<sub>1</sub> in a divider** → remember I<sub>1</sub> = I<sub>2</sub> + I<sub>B</sub>
- If the question says **"calculate the current I"** with a load in the collector → current source → the load value is irrelevant
- If a **Zener sets the base voltage** → V<sub>B</sub> = V<sub>rail</sub> + V<sub>Z</sub> directly, no KVL needed

**Chapter 1**

- If a **temperature in °C** appears → add 273 first, always
- If **n** is given → multiply it by V<sub>T</sub>, never by V<sub>D</sub>
- If **V<sub>D</sub> is negative** → the answer is −I<sub>s</sub>; stop, no calculator needed
- If you must **find V<sub>D</sub>** → use **ln**, never log₁₀

**Chapter 2**

- If a diode's **anode is more negative** than its cathode → OFF → I = 0 → V<sub>o</sub> = 0
- If **two diodes face each other** in one branch → that branch is an open circuit
- If **two diode branches meet** at a node → write KCL, then check both currents are positive
- If a **DC level is given** for a rectifier → work backwards: V<sub>m</sub> = V<sub>dc</sub>/0.318
- If a rectifier diode is **OFF** → the whole input appears **across the diode**
- If you see a **capacitor in series with the input** → clamper, not clipper
- If it is a **clamper** → find V<sub>C</sub> during the conducting half, then check the peak-to-peak matches
- If you see a **Zener** → do the removal test *before* assuming it regulates
- If **R<sub>L</sub> is fixed** and the question asks for a range → two cases: I<sub>Z</sub> = 0 and I<sub>Z</sub> = I<sub>Zmax</sub>

**Unit conversions — do these first, every time**

- kΩ → Ω: multiply by 1000  (2.2 kΩ = 2200 Ω)
- mA → A: divide by 1000  (2.5 mA = 0.0025 A)
- µA → A: divide by 1 000 000  (20 µA = 0.00002 A)
- **Shortcut:** volts ÷ kΩ = **mA** directly. (11.3 V ÷ 4 kΩ = 2.825 mA)
- **Shortcut:** kΩ × µF = **milliseconds**. (56 kΩ × 0.1 µF = 5.6 ms)
- mW → W: divide by 1000  (400 mW = 0.4 W)

## 4. Common Mistakes

**Unit and arithmetic slips**

1. **Forgetting to convert kΩ to Ω** before dividing — the single most common source of answers that are off by 1000.
2. **Mixing µA and mA** in the same equation. Convert everything to base units, or use the volts ÷ kΩ = mA shortcut consistently.
3. **Adding 273 to get Kelvin** — skipping this makes every Chapter 1 answer wrong.
4. **Using log instead of ln** when finding V<sub>D</sub>.

**Chapter 4 mistakes**

5. **Using R<sub>B</sub> alone when R<sub>E</sub> is present.** The denominator must be R<sub>B</sub> + (β+1)R<sub>E</sub>.
6. **Using (β+1) in the collector-feedback formula.** That one uses **β**, and it multiplies (R<sub>C</sub> + R<sub>E</sub>), not just R<sub>E</sub>.
7. **Forgetting I<sub>B</sub> when finding R<sub>1</sub>.** The current through R<sub>1</sub> is I<sub>2</sub> **+ I<sub>B</sub>** (see Q18).
8. **Using I<sub>C</sub> where I<sub>E</sub> belongs.** V<sub>E</sub> = I<sub>E</sub>R<sub>E</sub>, but V<sub>C</sub> = V<sub>CC</sub> − I<sub>C</sub>R<sub>C</sub>.
9. **Writing V<sub>CE</sub> = V<sub>C</sub>** when there is an R<sub>E</sub>. That shortcut only works if the emitter is grounded.
10. **Using the approximate divider method without checking Eq. (4.33)** — the exam often awards marks specifically for stating the check.
11. **Treating capacitors as shorts in a DC bias problem.** For DC they are **open**.
12. **Losing the sign of V<sub>E</sub>** in split-supply circuits. In Q34 the emitter sits at −2.55 V, below ground.
13. **Putting β into I<sub>Csat</sub>.** Saturation current has nothing to do with β.
14. **Forgetting to round to a standard value** in design questions when the question explicitly asks for it.

**Chapter 2 mistakes**

15. **Assuming a diode conducts without testing.** Always check the direction against the source polarity first — several questions here (Q5a, Q7b, Q9b) have the diode off.
16. **Misreading which battery terminal is which.** A "−" at the top of a battery makes the top node **negative**. This flips the answer entirely in Q5(a).
17. **Missing back-to-back diodes.** Two arrows facing each other mean the branch is dead — check before doing any algebra.
18. **Drawing v<sub>d</sub> as zero during the OFF half-cycle.** The entire input appears across the diode, so v<sub>d</sub> swings to −V<sub>m</sub>.
19. **Confusing 0.318 and 0.636.** Half-wave uses 0.318, full-wave uses 0.636.
20. **Subtracting one diode drop in a bridge.** Two diodes conduct at once, so subtract **2V<sub>K</sub>**.
21. **Confusing a clipper with a clamper.** A **capacitor in series** means clamper. Clipper cuts the waveform; clamper shifts it.
22. **Not checking the clamper peak-to-peak.** The output swing must equal the input swing — this catches nearly every sign error.
23. **Getting the sign of the battery wrong in a clipper.** Walk from the output node down through the branch and add the drops in order.
24. **Assuming the Zener is on.** Always compute V = V<sub>i</sub>R<sub>L</sub>/(R<sub>S</sub>+R<sub>L</sub>) first. In Q42(a) it is off.
25. **Forgetting that I<sub>R</sub> stays constant** while a Zener regulates — only I<sub>L</sub> and I<sub>Z</sub> trade current between them.
26. **Sizing R<sub>S</sub> at minimum load in a Zener design.** R<sub>S</sub> is set by the **maximum** load; the Zener's power rating is set by the **minimum** load.

## 5. Exam-Day Strategy

1. **Scan the whole paper first** and mark the type of each question in the margin. Types 7 (I<sub>Csat</sub>) and 3 (reverse-bias diode) take under a minute — do them first for guaranteed marks.
2. **Write the formula before substituting.** Most papers award a mark for the correct formula even if the arithmetic slips.
3. **Convert all units in one line** before you start calculating.
4. **Sanity-check every answer:**
   - I<sub>B</sub> should be in **µA**; I<sub>C</sub> in **mA**
   - V<sub>CE</sub> must be between 0 and V<sub>CC</sub> — if it is negative or larger than V<sub>CC</sub>, you have made an error
   - I<sub>CQ</sub> must be **less than** I<sub>Csat</sub>
   - V<sub>BC</sub> should be **negative** in the active region
   - A diode's forward voltage should land near 0.3–0.8 V
   - A clamper output must have the **same peak-to-peak swing** as its input
5. **Show the ON/OFF reasoning** for every diode. Even one line — "anode at −12 V, cathode at ground → reverse-biased → I = 0" — usually earns the mark.
6. **If a value seems missing**, say so explicitly and state the method. Never invent a number.
