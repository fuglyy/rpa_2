using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PR7_Sopina_RPA_Desktop_p1_varN28
{
    public partial class Form1 : Form
    {
        private int nextId = 1;

        public Form1()
        {
            InitializeComponent();
            btnAdd.Enabled = false; // Изначально кнопка неактивна
        }

        // Проверка, все ли поля заполнены
        private void CheckFormComplete()
        {
            bool isComplete = !string.IsNullOrWhiteSpace(txtPayment.Text) &&
                              !string.IsNullOrWhiteSpace(txtOperator.Text) &&
                              cmbMethod.SelectedItem != null &&
                              cmbPriority.SelectedItem != null;

            btnAdd.Enabled = isComplete;
        }

        // Событие при изменении текста в Payment
        private void txtPayment_TextChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        // Событие при изменении текста в Operator
        private void txtOperator_TextChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        // Событие при выборе метода оплаты
        private void cmbMethod_SelectedIndexChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        // Событие при выборе приоритета
        private void cmbPriority_SelectedIndexChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        // Кнопка Add
        private void btnAdd_Click(object sender, EventArgs e)
        {
            // Добавляем строку в таблицу
            dgvPayments.Rows.Add(
                nextId++,
                txtPayment.Text,
                txtOperator.Text,
                cmbMethod.SelectedItem.ToString(),
                cmbPriority.SelectedItem.ToString(),
                "New"
            );

            // Очищаем поля (но не таблицу)
            ClearFormFields();
        }

        // Кнопка Clear Form
        private void btnClear_Click(object sender, EventArgs e)
        {
            ClearFormFields();
        }

        // Очистка полей формы
        private void ClearFormFields()
        {
            txtPayment.Text = "";
            txtOperator.Text = "";
            cmbMethod.SelectedIndex = -1;
            cmbPriority.SelectedIndex = -1;
            btnAdd.Enabled = false;
        }
    }
}
