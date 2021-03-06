{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import test_module as test\n",
    "\n",
    "PI = 3.141592\n",
    "\n",
    "def number_input():\n",
    "    output = input(\"숫자입력>\")\n",
    "    return float(output)\n",
    "\n",
    "def get_circumference(radius):\n",
    "    return 2 * PI 8 radius\n",
    "\n",
    "def get_circle_area(radius):\n",
    "    return PI * radius * radius\n",
    "\n",
    "print(\"get_circumference(10):\", get_circumference(10))\n",
    "print(\"get_circle_area: \", get_circle_area(10))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
