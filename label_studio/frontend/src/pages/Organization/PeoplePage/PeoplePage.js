import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { LsPlus } from "../../../assets/icons";
import { Button, Dropdown } from "../../../components";
import { Description } from "../../../components/Description/Description";
import { Input } from "../../../components/Form";
import { modal } from "../../../components/Modal/Modal";
import { Space } from "../../../components/Space/Space";
import { useAPI } from "../../../providers/ApiProvider";
import { useConfig } from "../../../providers/ConfigProvider";
import { Block, Elem } from "../../../utils/bem";
import { copyText } from "../../../utils/helpers";
import "./PeopleInvitation.styl";
import { PeopleList } from "./PeopleList";
//import { InvitedList } from "./InvitedList";
import "./PeoplePage.styl";
import { SelectedUser } from "./SelectedUser";
import { InvitedList } from "./InvitedList";
// TODO: Chạy được npm start :<<<

// state = {
//   pk: 0,
//   email: "",
//   role: "",
//   invited_at: "",
//   role : [
//     {key:'1',value:'Administrator'},
//     {key:'2',value:'Manager'},
//     {key:'3',value:'Annotator'},
//   ]
// };


const InvitationModal = ({ link }) => {
// TODO: Chỗ này sửa nha, thêm cái form để add người vô, viết cái API lấy role có nhỏ cấp hơn cấp của user hiện tại, vs hoàn thiện cái API post add người
  const api = useAPI();
  const [invitedEmail, setEmail] = useState("")
  const [roleid, setRole] = useState("0")
  const [roleList, setRoleList] = useState([{'name':'','id':''}])
  const [errorMessage, setErrorMessage] = useState('');
  const [stateMessage, setStateMessage] = useState('');

  useEffect(() =>{
      const fetchData = async ()=>{
          const response = await api.callApi('listrole')
          const newData = await response;
          setRoleList(newData);
      };
      fetchData();
  }, [])

  const handleChange = (event) =>{
      setRole(event.target.value);
  }

  function isValidEmail(email) {
    return /\S+@\S+\.\S+/.test(email);
  }

  const saveBtn = async (e) => {
      e.preventDefault();

      if (invitedEmail.trim().length == 0)
      {
        setErrorMessage('Email is empty!!');
        return;
      }
      else
      {
        if (!isValidEmail(invitedEmail))
        {
          setErrorMessage('Email format is incorrect!!');
          return;
        }
        else
          setErrorMessage(null);
      }
      
      console.log(roleid)
      if (roleid=='0')
      {
          setErrorMessage('Please choose Role!!');
          return;
      }
      else
        setErrorMessage(null);

      // console.log('Email',invitedEmail);
      // console.log('Role',roleid);
      if (invitedEmail && roleid)
      {
        const response = await api.callApi('addperson',
        {
          body: {
            email: invitedEmail,
            role: roleid,
          },
        }
        );
        if (response)
          if (response.state == 'success')
            setStateMessage("Successfully add person to organization")
          else
          {
            setStateMessage(null)
            setErrorMessage(response.error)
          }
        else
          setErrorMessage("Fail to send request")
      }
    }
  return (
    <Block name="invite">
      <Elem name="title"> Invite Link</Elem>
      <Input
        value={link}
        style={{ width: '100%' }}
        readOnly
      />
      <form onSubmit={saveBtn}>
      <Elem name="title" > Email </Elem>
      <Input
            type="text"
            name="email"
            style={{ width: '100%' }}
            placeholder="Enter email of invited person"
            value={invitedEmail}
            onChange={e=> setEmail(e.target.value)}
            //value={this.defaultIfEmpty(this.state.name)}
      />
      
      <Elem name="title"> Role </Elem>
      <select style={{ width:'100%',fontSize: 16, minHeight:40 }} value={roleid} onChange={handleChange}>
        <option value='0' disabled>Choose Role here</option>
        {roleList.map(role => 
        (
                <option value={role.id} key={role.id}>{role.name}</option>
          ))
        }
      </select>

      <Button style={{ width: 170, marginTop: 20, background: 'rgb(226 166 109)' }} type="submit">
          Add
      </Button>
      {errorMessage && (
          <i className="error" style={{color: 'rgb(228 46 46)'}}> {errorMessage} </i>
            )}

      {stateMessage && (
          <i className="state" style={{color: 'rgb(64 184 49)'}}> {stateMessage} </i>
            )}
      </form>

    </Block>
  );
};

export const PeoplePage = () => {
  const api = useAPI();
  const inviteModal = useRef();
  const config = useConfig();
  const [selectedUser, setSelectedUser] = useState(null);
  const [link, setLink] = useState();

  const selectUser = useCallback((user) => {
    setSelectedUser(user);
    localStorage.setItem('selectedUser', user?.id);
  }, [setSelectedUser]);

  const setInviteLink = useCallback((link) => {
    const hostname = config.hostname || location.origin;
    setLink(`${hostname}${link}`);
  }, [config, setLink]);

  const updateLink = useCallback(() => {
    api.callApi('resetInviteLink').then(({ invite_url }) => {
      setInviteLink(invite_url);
    });
  }, [setInviteLink]);

  const inviteModalProps = useCallback((link) => ({
    title: "Invite people",
    style: { width: 640, height: 472 },
    body: () => (
      <InvitationModal link={link}/>
    ),
    footer: () => {
      const [copied, setCopied] = useState(false);

      const copyLink = useCallback(() => {
        setCopied(true);
        copyText(link);
        setTimeout(() => setCopied(false), 1500);
      }, []);

      return (
        <Space spread>
          <Space>
            <Button style={{ width: 170 }} onClick={() => updateLink()}>
              Reset Link
            </Button>
          </Space>
          <Space>
            <Button primary style={{ width: 170 }} onClick={copyLink}>
              {copied ? "Copied!" : "Copy link"}
            </Button>
          </Space>
        </Space>
      );
    },
    bareFooter: true,
  }), []);

  const showInvitationModal = useCallback(() => {
    inviteModal.current = modal(inviteModalProps(link));
  }, [inviteModalProps, link]);

  const defaultSelected = useMemo(() => {
    return localStorage.getItem('selectedUser');
  }, []);

  useEffect(() => {
    api.callApi("inviteLink").then(({ invite_url }) => {
      setInviteLink(invite_url);
    });
  }, []);

  useEffect(() => {
    inviteModal.current?.update(inviteModalProps(link));
  }, [link]);

  return (
    <Block name="people">
      <Elem name="controls">
        <Space spread>
          <Space></Space>

          <Space>
            <Button icon={<LsPlus/>} primary onClick={showInvitationModal}>
              Add People
            </Button>
          </Space>
        </Space>
      </Elem>

      <Elem name="title"> 
        Organization's Members List 
        </Elem>
      <Elem name="content">
        <PeopleList
          selectedUser={selectedUser}
          defaultSelected={defaultSelected}
          onSelect={(user) => selectUser(user)}
        />
        {selectedUser && (
          <SelectedUser
            user={selectedUser}
            onClose={() => selectUser(null)}
          />
        )}
      </Elem>
      <Elem name="title"> Invited Members List </Elem>
      <Elem name="content">
        <InvitedList
        />
      </Elem>
    </Block>
  );
};

PeoplePage.title = "People";
PeoplePage.path = "/";
