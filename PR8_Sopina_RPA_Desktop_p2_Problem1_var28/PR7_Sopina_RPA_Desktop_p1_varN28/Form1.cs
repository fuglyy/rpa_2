using System;
using System.Windows.Forms;

namespace PR7_Sopina_RPA_Desktop_p1_varN28
{
    public partial class Form1 : Form
    {
        private int nextId = 1;

        public Form1()
        {
            InitializeComponent();
            dgvPayments.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            btnAdd.Enabled = false;
            btnConfirmPayment.Enabled = false;
            btnAssignOperator.Enabled = false;
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

        // Проверка, выбрана ли строка в таблице
        private void CheckRowSelected()
        {
            bool rowSelected = dgvPayments.SelectedRows.Count > 0;

            if (rowSelected)
            {
                DataGridViewRow selectedRow = dgvPayments.SelectedRows[0];

                // Проверяем статус для кнопки Confirm Payment
                if (dgvPayments.Columns.Contains("colStatus"))
                {
                    string currentStatus = selectedRow.Cells["colStatus"].Value?.ToString() ?? "New";
                    btnConfirmPayment.Enabled = (currentStatus != "Confirmed");
                }
                else
                {
                    btnConfirmPayment.Enabled = true;
                }

                // Assign Operator всегда активен при выборе строки
                btnAssignOperator.Enabled = true;
            }
            else
            {
                btnConfirmPayment.Enabled = false;
                btnAssignOperator.Enabled = false;
            }
        }

        // Событие при изменении выбора строки
        private void dgvPayments_SelectionChanged(object sender, EventArgs e)
        {
            CheckRowSelected();
        }

        // События при изменении полей формы
        private void txtPayment_TextChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        private void txtOperator_TextChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        private void cmbMethod_SelectedIndexChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        private void cmbPriority_SelectedIndexChanged(object sender, EventArgs e)
        {
            CheckFormComplete();
        }

        // Кнопка Add
        private void btnAdd_Click(object sender, EventArgs e)
        {
            dgvPayments.Rows.Add(
                nextId++,
                txtPayment.Text,
                txtOperator.Text,
                cmbMethod.SelectedItem.ToString(),
                cmbPriority.SelectedItem.ToString(),
                "New"
            );

            ClearFormFields();
        }

        // Кнопка Clear Form
        private void btnClear_Click(object sender, EventArgs e)
        {
            ClearFormFields();
        }

        // Кнопка Confirm Payment - МЕНЯЕТ СТАТУС
        private void btnConfirmPayment_Click(object sender, EventArgs e)
        {
            if (dgvPayments.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dgvPayments.SelectedRows[0];

                // Меняем статус на "Confirmed"
                selectedRow.Cells["colStatus"].Value = "Confirmed";

                // Обновляем состояние кнопок (Confirm Payment должна стать неактивной)
                CheckRowSelected();
            }
        }

        // Кнопка Assign Operator - НАЗНАЧАЕТ ОПЕРАТОРА
        private void btnAssignOperator_Click(object sender, EventArgs e)
        {
            if (dgvPayments.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dgvPayments.SelectedRows[0];
                string operatorName = txtOperator.Text;

                if (!string.IsNullOrWhiteSpace(operatorName))
                {
                    // Записываем имя оператора в колонку Operator
                    selectedRow.Cells["colOperator"].Value = operatorName;

                }
            }
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